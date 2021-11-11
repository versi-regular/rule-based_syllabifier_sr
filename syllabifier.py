from srtools import latin_to_cyrillic, cyrillic_to_latin
from get_indices import get_sound_type_indices


def syllabify(text):
	transliterated_text = latin_to_cyrillic(text)
	words = text_to_words(transliterated_text)

	syllabified_words = [word_to_syllables(word, get_sound_type_indices(word)) for word in words]

	syllabified_text = " ".join(syllabified_words)

	return cyrillic_to_latin(syllabified_text)


def word_to_syllables(word, sound_structure):

	nuclei_positions, sonant_positions, fricative_positions, africate_positions, nasal_positions, plosive_positions = sound_structure

	i = 0
	sound_list = list(word)

	# SYLLABLE BOUNDARY COMES AFTER A SYLLABLE NUCLEUS, BEFORE A CONSONANT
	## except if it is the last syllable nucleus in the word
	for position in nuclei_positions[:-1]:
		i += 1
		# MEDIALLY, IF A CLUSTER STARTS WITH 2 SONANTS, THE BOUNDARY WILL BE BETWEEN THEM
		## implemented as an exception to the general rule
		## defined as applicable following a vowel
		if position + 1 in sonant_positions and position + 2 in sonant_positions:
			# DO NOT SEPARATE A PRECEDING CONSONANT FROM je IN THE IJEKAVICA DIALECT
			if word[position + 2] =="ј" and word[position + 3] == "е":
				sound_list.insert(position + i, "-")
			else:
				sound_list.insert(position + i + 1, "-")
		# BOUNDARY WILL BE BETWEEN A PLOSIVE FOLLOWED AND A CONSONANT THAT IS NOT ONE OF THE SONANTS j, v, l, lj and r
		## implemented as an exception to the general rule
		## defined as applicable following a vowel
		elif (position + 1 in plosive_positions or position + 1 in nasal_positions) and (position + 2 in fricative_positions or position + 2 in plosive_positions or position + 2 in africate_positions or position + 2 in nasal_positions):
			sound_list.insert(position + i + 1, "-")
		else:
			sound_list.insert(position + i, "-")

	syllabified_word = "".join(sound_list)

	ssp_syllabified_word = ssp(word, syllabified_word, nuclei_positions)
	ssp_syllabified_word2 = ssp(word, ssp_syllabified_word, nuclei_positions)

	return ssp_syllabified_word2


def ssp(word, syllabified_word, nuclei_positions):
	"""Returns a re-segmented syllabified word that is in alignment with the Sonority Sequencing Principle."""
	alphabets = (u"АЕОИУJЈРЛЉМНЊСВЗЖШФХЏЂЦЧЋБДГПТКаеоиуjјрлљмнњсвзжшфхџђцчћбдгптк-", u"АЕОИУ00011222344455566777888999аеоиу00011222344455566777888999-")
	transliterator = {ord(cyrillic):ord(sonority) for cyrillic, sonority in zip(*alphabets)}

	word_sonority = syllabified_word.translate(transliterator)
	word_syllable_structure = get_syllable_structure(word, syllabified_word, nuclei_positions)
	syllables = syllabified_word.split("-")
	syllable_sonority = word_sonority.split("-")
	syllable_structure = word_syllable_structure.split("-")

	for i in range(len(syllables)):
		if len(syllables[i]) > 1 and "V" in syllable_structure[i]:
			# if there is an element of higher sonority at the edge
			if i != 0 and syllable_structure[i][0] != "V" and syllable_structure[i][1] != "V" and syllable_sonority[i][0] < syllable_sonority[i][1] and syllable_sonority[i][0:2] not in ["39", "59", "48", "37", "57", "46"]:
				syllables[i-1] = syllables[i-1] + syllables[i][0]
				syllables[i] = syllables[i][1:]
			# if syllable_sonority[i][-1] < syllable_sonority[i][-2] and syllable_structure[i][-1] != "V":
			# 	syllables[i+1] = syllables[i][-1] + syllables[i+1]
			# 	syllables[i] = syllables[i][:-1]

	spp_syllabified_word = "-".join(syllables)

	return spp_syllabified_word


def get_syllable_structure(word, syllabified_word, nuclei_positions):
	"""Returns the CV syllable structure of a syllabified word."""

	separator_positions = [v for v, letter in enumerate(syllabified_word) if letter == "-"]

	word_list = list(word)

	for i in range(len(word_list)):
		if i in nuclei_positions:
			word_list[i] = "V"
		else:
			word_list[i] ="C"

	for position in separator_positions:
		word_list.insert(position, "-")

	return "".join(word_list)

def text_to_words(text):
	return text.split(" ")
