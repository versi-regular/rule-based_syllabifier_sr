import re


def get_sound_type_indices(word):
	nuclei = find_syllable_nuclei(word)
	sonants = find_sonants(word)
	fricatives = find_fricatives(word)
	africates = find_africates(word)
	nasals = find_nasals(word)
	plosives = find_plosives(word)

	return nuclei, sonants, fricatives, africates, nasals, plosives


def find_syllable_nuclei(word):
	return sorted(find_vowels(word) | find_syllabic_consonants(word))


def find_vowels(word):
	return {position.start() for position in re.finditer("[АЕИОУаеиоу]", word)}


def find_syllabic_consonants(word):
	syllabic_r = find_syllabic_r(word)
	syllabic_l = find_syllabic_l(word)
	syllabic_n = find_syllabic_n(word)
	return set(syllabic_r | syllabic_l | syllabic_n)


def find_syllabic_r(word):
	return {position.start() for position in re.finditer(
		"((?<=^)|(?<=[БВГДЂЖЗЈКЛЉМНЊПСТЋФХЦЧЏШбвгдђжзјклљмнњпстћфхцчџш]))[Рр]([БВГДЂЖЗКЛЉМНЊПСТЋФХЦЧЏШбвгдђжзклљмнњпстћфхцчџш]|[Jј](!?=е))",
		word)}


def find_syllabic_l(word):
	return {position.start() for position in re.finditer(
		"((?<=^)|(?<=[БВГДЂЖЗКЉМНЊПСТЋФХЦЧЏШбвгдђжзкљмнњпстћфхцчџш]))[Лл]([БВГДЂЖЗКЉМНЊПСТЋФХЦЧЏШбвгдђжзкљмнњпстћфхцчџш]|(?=$))",
		word)}


def find_syllabic_n(word):
	return {position.start() for position in re.finditer(
		"((?<=^)|(?<=[БВГДЂЖЗКЉМЊПСТЋФХЦЧЏШбвгдђжзкљмњпстћфхцчџш]))[Нн]([БВГДЂЖЗКЉМЊПСТЋФХЦЧЏШбвгдђжзкљмњпстћфхцчџш]|(?=$))",
		word)}


def find_sonants(word):
	return sorted({position.start() for position in re.finditer("[ВЈЛЉМНЊРвјлљмнњр]", word)} - (find_syllabic_consonants(word)))


def find_fricatives(word):
	return {position.start() for position in re.finditer("[СЖЗШФХсжзшфх]", word)}


def find_africates(word):
	return {position.start() for position in re.finditer("[ЦЧЋЏЂцчћџђ]", word)}


def find_nasals(word):
	return {position.start() for position in re.finditer("[МНЊмнњ]", word)}


def find_plosives(word):
	return {position.start() for position in re.finditer("[БПГКДТбпгкдт]", word)}
