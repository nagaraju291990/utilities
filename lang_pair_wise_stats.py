import sys
import re

fp = open(sys.argv[1], "r", encoding="utf-8")
lines = fp.read().split("\n")
fp.close()


lang_pair_hash = {}
for  line in lines[1:]:
	line = re.sub(r'","', '"\t"', line)
	line = re.sub(r'"',"",line)
	if(line == ""):
		continue
	cols = line.split("\t")
	if(len(cols) < 6):
		continue
	filename_langpair = cols[1]
	lang_pair = filename_langpair.split("____")[-1]
	#print(lang_pair)
	wc = int(cols[5])
	if lang_pair in lang_pair_hash:
		current_words = lang_pair_hash[lang_pair]
		lang_pair_hash[lang_pair] = current_words + wc
	else:
		lang_pair_hash[lang_pair] = wc


for lp in lang_pair_hash:
	print(lp, lang_pair_hash[lp],sep='\t')
