import re

def find_consonants(word):
	"""Returns a list triple of the positional indices ls, ns, and rs."""

	sonant_positions = sorted({position.start() for position in re.finditer("[ВЈЛЉМНЊРвјлљмнњр]", word)} - (find_syllabic_consonants(word)))
	fricative_positions = {position.start() for position in re.finditer("[СЖЗШФХсжзшфх]", word)}
	africate_positions = {position.start() for position in re.finditer("[ЦЧЋЏЂцчћџђ]", word)}
	nasal_positions = {position.start() for position in re.finditer("[МНЊмнњ]", word)}
	plosive_positions = {position.start() for position in re.finditer("[БПГКДТбпгкдт]", word)}

	return sonant_positions, fricative_positions, africate_positions, nasal_positions, plosive_positions


def find_vowels(word):
	""" Returns a list of the positional indices of vowels."""

	vowels_positions = {position.start() for position in re.finditer("[аеиоу]", word)}

	return vowels_positions


def find_syllabic_consonants(word):
	"""Returns a list of the positional indices of syllabic consonants."""

	# r in lower sonority contexts (exlude words with double r)
	syllabic_r = {position.start() for position in re.finditer("((?<=^)|(?<=[БВГДЂЖЗЈКЛЉМНЊПСТЋФХЦЧЏШбвгдђжзјклљмнњпстћфхцчџш]))р([БВГДЂЖЗКЛЉМНЊПСТЋФХЦЧЏШбвгдђжзклљмнњпстћфхцчџш]|[Jј](!?=е))", word)}
	# l in lower sonority contexts (exclude words with double l)
	syllabic_l = {position.start() for position in re.finditer("((?<=^)|(?<=[БВГДЂЖЗКЉМНЊПСТЋФХЦЧЏШбвгдђжзкљмнњпстћфхцчџш]))л([БВГДЂЖЗКЉМНЊПСТЋФХЦЧЏШбвгдђжзкљмнњпстћфхцчџш]|(?=$))", word)}
	# n in lower sonority contexts (exclude words with double n)
	syllabic_n = {position.start() for position in re.finditer("((?<=^)|(?<=[БВГДЂЖЗКЉМЊПСТЋФХЦЧЏШбвгдђжзкљмњпстћфхцчџш]))н([БВГДЂЖЗКЉМЊПСТЋФХЦЧЏШбвгдђжзкљмњпстћфхцчџш]|(?=$))", word)}
	
	return set(syllabic_r | syllabic_l | syllabic_n)


def find_syllable_nuclei(word):
	"""Returns a list of positional indices of syllable nuclei."""

	return sorted(find_vowels(word) | find_syllabic_consonants(word))