import sys
import re

fp = open(sys.argv[1], "r", encoding="utf-8")
lines = fp.read().split("\n")
fp.close()


taskid_hash = {}
for  line in lines:
	if(line == ""):
		continue
	cols = line.split("\t")
	if(len(cols) < 6):
		continue
	source = cols[0]
	target = cols[1]
	taskid = cols[3]
	lang_pair = cols[2]
	print(lang_pair)
	if taskid in taskid_hash:
		fp1.write(source + "\n")
		fp2.write(target + "\n")
	else:
		taskid_hash[taskid] = 1
		if(lang_pair == "eng_hin" or lang_pair == "eng_tel" or lang_pair == "eng_mal" or lang_pair == "eng_kan" or lang_pair == "eng_ben"):
			fp1 = open(lang_pair +'/source_'+taskid + '.txt', 'w', encoding='utf-8')
			fp2 = open(lang_pair +'/target_'+taskid + '.txt', 'w', encoding='utf-8')
			fp1.write(source + "\n")
			fp2.write(target + "\n")
