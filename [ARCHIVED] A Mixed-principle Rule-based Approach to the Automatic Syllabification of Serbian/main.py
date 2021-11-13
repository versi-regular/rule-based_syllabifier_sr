# -*- coding: utf-8 -*-

import os, re
from transliterator import transliterate
from find_indices import find_syllable_nuclei, find_consonants
from rule_based_syllabifier import syllabify, get_syllable_structure

if __name__ == "__main__":

	# list SrpLemKor files
	corpus_folder = os.path.join(".", "..", "SrpLemKor", "texts", "")
	files = [f for f in os.listdir(corpus_folder) if f not in ["260.txt", "4505.txt","4517.txt"]]

	# loop through the files
	for f in files:
		with open(corpus_folder + f) as text:
			for line in text:

				try:
					# exclude RN, ABB, NUM @card@, SENT, PUNCT and ? tags
					word = line.split()[0]
					pos = line.split()[-2]
					if pos == "NUM" and line.split()[-1] == "@card@" or pos in ["PUNCT", "ABB", "RN", "SENT", "?"] or "q" in word or "w" in word:
						continue				
				except:
					pass

				# to single-character Cyrillic
				word = transliterate(word)
				if "x" in word or "y" in word:
					continue
				# find letter indices
				nuclei_positions = find_syllable_nuclei(word)
				sonant_positions, fricative_positions, africate_positions, nasal_positions, plosive_positions = find_consonants(word)

				# sillabify
				syllabified_word = syllabify(word, nuclei_positions, sonant_positions, fricative_positions, africate_positions, nasal_positions, plosive_positions)

				# get structure
				syllable_structure = get_syllable_structure(word, syllabified_word, nuclei_positions)
				

				# output
				#print(syllabified_word + "\t" + syllable_structure)