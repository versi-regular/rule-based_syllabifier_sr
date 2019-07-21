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
			nucleus_position = syllableStructureList[0].find("V")
			try:
				monosyllabic[syllabifiedWordList[0][nucleus_position].lower()] += 1
			except:
				monosyllabic[syllabifiedWordList[0][nucleus_position].lower()] = 1

		elif len(syllabifiedWordList) > 1:
			nucleus_position = syllableStructureList[0].find("V")
			try:
				polysyllabic_initial[syllabifiedWordList[0][nucleus_position].lower()] += 1
			except:
				polysyllabic_initial[syllabifiedWordList[0][nucleus_position].lower()] = 1
			nucleus_position = syllableStructureList[-1].find("V")
			try:
				polysyllabic_final[syllabifiedWordList[-1][nucleus_position].lower()] += 1
			except:
				polysyllabic_final[syllabifiedWordList[-1][nucleus_position].lower()] = 1

			if len(syllabifiedWordList) > 2:
				for i in range(1, len(syllabifiedWordList)-1):
					nucleus_position = syllableStructureList[i].find("V")
					try:
						polysyllabic_medial[syllabifiedWordList[i][nucleus_position].lower()] += 1
					except:
						polysyllabic_medial[syllabifiedWordList[i][nucleus_position].lower()] = 1

# for key in monosyllabic.keys():
# 	print(key + "\t" + str(monosyllabic[key]))

# for key in polysyllabic_initial.keys():
# 	print(key + "\t" + str(polysyllabic_initial[key]))

for key in polysyllabic_medial.keys():
	print(key + "\t" + str(polysyllabic_medial[key]))

# for key in polysyllabic_final.keys():
# 	print(key + "\t" + str(polysyllabic_final[key]))