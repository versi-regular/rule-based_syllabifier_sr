def syllabify(word, nuclei_positions, sonant_positions, fricative_positions, africate_positions, nasal_positions, plosive_positions):
	"Descriptive rule-based syllabifier for Serbian."

	i = 0
	word_list = list(word)

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
				word_list.insert(position + i, "-")
			else:
				word_list.insert(position + i + 1, "-")
		# BOUNDARY WILL BE BETWEEN A PLOSIVE FOLLOWED AND A CONSONANT THAT IS NOT ONE OF THE SONANTS j, v, l, lj and r
		## implemented as an exception to the general rule
		## defined as applicable following a vowel
		elif (position + 1 in plosive_positions or position + 1 in nasal_positions) and (position + 2 in fricative_positions or position + 2 in plosive_positions or position + 2 in africate_positions or position + 2 in nasal_positions):
			word_list.insert(position + i + 1, "-")
		else:
			word_list.insert(position + i, "-")

	syllabified_word = "".join(word_list)

	return syllabified_word


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

	syllable_structure = "".join(word_list)

	return syllable_structure