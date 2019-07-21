monosyllabic = dict()
polysyllabic_initial = dict()
polysyllabic_medial = dict()
polysyllabic_final = dict()

with open("syllabified.txt", "r") as syllabifierOutput:
	for line in syllabifierOutput:
		syllabifiedWord, syllableStructure = line.strip().split("\t")
		syllabifiedWordList = syllabifiedWord.split("-")
		syllableStructureList = syllableStructure.split("-")

		if len(syllabifiedWordList) == 1 and "V" in syllableStructure:
			try:
				monosyllabic[syllableStructureList[0]] += 1
			except:
				monosyllabic[syllableStructureList[0]] = 1

		elif len(syllabifiedWordList) > 1:
			try:
				polysyllabic_initial[syllableStructureList[0]] += 1
			except:
				polysyllabic_initial[syllableStructureList[0]] = 1
			try:
				polysyllabic_final[syllableStructureList[-1]] += 1
			except:
				polysyllabic_final[syllableStructureList[-1]] = 1

			if len(syllabifiedWordList) > 2:
				for i in range(1, len(syllabifiedWordList)-1):
					try:
						polysyllabic_medial[syllableStructureList[i]] += 1
					except:
						polysyllabic_medial[syllableStructureList[i]] = 1

# for key in monosyllabic.keys():
# 	print(key + "\t" + str(monosyllabic[key]))

# for key in polysyllabic_initial.keys():
# 	print(key + "\t" + str(polysyllabic_initial[key]))

# for key in polysyllabic_medial.keys():
# 	print(key + "\t" + str(polysyllabic_medial[key]))

# for key in polysyllabic_final.keys():
# 	print(key + "\t" + str(polysyllabic_final[key]))