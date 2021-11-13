from srtools import latin_to_cyrillic, cyrillic_to_latin
from source.get_indices import get_sound_type_indices


def syllabify(text):
    transliterated_text = latin_to_cyrillic(text)
    words = transliterated_text.split(" ")

    syllabified_words = [apply_ssp(word, apply_ssp(word, word_to_syllables(word)))
                         if "--" not in apply_ssp(word, apply_ssp(word, word_to_syllables(word)))
                         else word for word in words]

    syllabified_text = " ".join(syllabified_words)

    if transliterated_text == text:
        return syllabified_text
    else:
        return cyrillic_to_latin(syllabified_text)


def word_to_syllables(word):
    nuclei_positions, sonant_positions, fricative_positions, \
        africate_positions, nasal_positions, plosive_positions = get_sound_type_indices(word)

    phoneme_list = list(word)
    i = 0

    # SYLLABLE BOUNDARY COMES AFTER A SYLLABLE NUCLEUS, BEFORE A CONSONANT
    # except if it is the last syllable nucleus in the word
    for position in nuclei_positions[:-1]:
        i += 1
        # MEDIALLY, IF A CLUSTER STARTS WITH 2 SONANTS, THE BOUNDARY WILL BE BETWEEN THEM
        # implemented as an exception to the general rule
        # defined as applicable following a vowel
        if position + 1 in sonant_positions and position + 2 in sonant_positions:
            # DO NOT SEPARATE A PRECEDING CONSONANT FROM je IN THE IJEKAVICA DIALECT
            if word[position + 2] == "ј" and word[position + 3] == "е":
                phoneme_list.insert(position + i, "-")
            else:
                phoneme_list.insert(position + i + 1, "-")
        # BOUNDARY WILL BE BETWEEN A PLOSIVE FOLLOWED AND A CONSONANT THAT IS NOT ONE OF THE SONANTS j, v, l, lj and r
        # implemented as an exception to the general rule
        # defined as applicable following a vowel
        elif (position + 1 in plosive_positions.union(nasal_positions)) and \
                (position + 2 in set.union(
                    *[fricative_positions, plosive_positions, africate_positions, nasal_positions])):
            phoneme_list.insert(position + i + 1, "-")
        else:
            phoneme_list.insert(position + i, "-")

    syllabified_word = "".join(phoneme_list)

    return syllabified_word


def apply_ssp(word, syllabified_word):
    syllables = syllabified_word.split("-")
    syllable_sonority = word_to_sonority_structure(syllabified_word).split("-")
    syllable_structure = get_syllable_structure(word, syllabified_word).split("-")

    for i in range(len(syllables)):
        if len(syllables[i]) > 1 and "V" in syllable_structure[i]:
            # if there is an element of higher sonority at the edge, move it to the preceding syllable
            if i != 0 and syllable_structure[i][0] != "V" and syllable_structure[i][1] != "V" \
                    and syllable_sonority[i][0] < syllable_sonority[i][1] \
                    and syllable_sonority[i][0:2] not in ["39", "59", "48", "37", "57", "46"] \
                    and syllables[i - 1] != "":
                syllables[i - 1] = syllables[i - 1] + syllables[i][0]
                syllables[i] = syllables[i][1:]

    spp_syllabified_word = "-".join(syllables)

    return spp_syllabified_word


def word_to_sonority_structure(word):
    alphabets = (u"АЕОИУJЈРЛЉМНЊСВЗЖШФХЏЂЦЧЋБДГПТКаеоиуjјрлљмнњсвзжшфхџђцчћбдгптк-",
                 u"АЕОИУ00011222344455566777888999аеоиу00011222344455566777888999-")
    transliterator = {ord(cyrillic): ord(sonority) for cyrillic, sonority in zip(*alphabets)}

    return word.translate(transliterator)


def get_syllable_structure(word, syllabified_word):
    nuclei_positions, *_ = get_sound_type_indices(word)
    separator_positions = [v for v, letter in enumerate(syllabified_word) if letter == "-"]

    phoneme_list = list(word)

    for i in range(len(phoneme_list)):
        if i in nuclei_positions:
            phoneme_list[i] = "V"
        else:
            phoneme_list[i] = "C"

    for position in separator_positions:
        phoneme_list.insert(position, "-")

    return "".join(phoneme_list)
