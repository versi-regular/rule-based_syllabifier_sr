def transliterate(word):
	"""Transliterates the Latin letters and digraphs of SrpLemKor into the Cyrillic alphabet."""

	alphabets = (u"abvgdђeжzijklљmnњoprstћufhcчџш", u"абвгдђежзијклљмнњопрстћуфхцчџш")
	transliterator = {ord(latin):ord(cyrillic) for latin, cyrillic in zip(*alphabets)}

	word = word.replace("cx", "ћ").replace("cy", "ч").replace("dx", "ђ").replace("dy", "џ").replace("lx", "љ").replace("nx", "њ").replace("sx", "ш").replace("zx", "ж")

	word = word.translate(transliterator)

	return word