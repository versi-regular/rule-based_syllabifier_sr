import re

def find_rln(word):
	"""Returns a list triple of the positional indices ls, ns, and rs."""
	
	l_positions = [position.start() for position in re.finditer("л", word)]
	n_positions = [position.start() for position in re.finditer("н", word)]
	r_positions = [position.start() for position in re.finditer("р", word)]

	return l_positions, n_positions, r_positions


def find_vowels(word):
	""" Returns a list of the positional indices of vowels."""

	vowels_positions = sorted([position.start() for position in re.finditer("аеиоу", word)])

	return vowels_positions


def find_syllabic_consonants(word):
	"""Returns a list of the positional indices of syllabic consonants."""

	# r in lower sonority contexts (exlude words with double r)
	syllabic_r = [position.start() for position in re.finditer("((?<=^)|(?<=[БВГДЂЖЗЈКЛЉМНЊПСТЋФХЦЧЏШбвгдђжзјклљмнњпстћфхцчџш]))р([БВГДЂЖЗКЛЉМНЊПСТЋФХЦЧЏШбвгдђжзклљмнњпстћфхцчџш]|[Jј](!?=е))", word)]

	# l in lower sonority contexts (exclude words with double l)
	syllabic_l = [position.start() for position in re.finditer("((?<=^)|(?<=[БВГДЂЖЗКЉМНЊПСТЋФХЦЧЏШбвгдђжзкљмнњпстћфхцчџш]))л([БВГДЂЖЗКЉМНЊПСТЋФХЦЧЏШбвгдђжзкљмнњпстћфхцчџш]|(?=$))", word)]
				
	# n in lower sonority contexts (exclude words with double n)
	syllabic_n = [position.start() for position in re.finditer("((?<=^)|(?<=[БВГДЂЖЗКЉМЊПСТЋФХЦЧЏШбвгдђжзкљмњпстћфхцчџш]))н([БВГДЂЖЗКЉМЊПСТЋФХЦЧЏШбвгдђжзкљмњпстћфхцчџш]|(?=$))", word)]
	
	return syllabic_r + syllabic_l + syllabic_n