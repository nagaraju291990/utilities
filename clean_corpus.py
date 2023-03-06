import re
import sys

given_file = sys.argv[1]

fp1 = open(given_file,'r')
lines = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file

out_hash = {}
for line in lines:

	line = re.sub(r'\uFFFD', "-", line, flags = re.MULTILINE) #replacement character
	line = re.sub(r'\u000C', "", line, flags = re.MULTILINE)	#formfeed
	line = re.sub(r'\u00A0'," ", line, flags = re.MULTILINE)    #convert nbsp space to normal space
	line = re.sub(r'^ *',"", line, flags = re.MULTILINE)
	line = re.sub(r' *$',"", line, flags = re.MULTILINE)
	line = re.sub(r' +', " ", line, flags = re.MULTILINE)
	
	cols = line.split("\t")

	if(re.search(r'[\u0900-\u09FF]', cols[0])):	#check for hindi unicode
		src_sentence = cols[0]
		if(len(src_sentence.split(" ")) < 100):	#check word count > 100
			out_hash[src_sentence] = cols[1]	#makes unique


for k in out_hash:
	print(k, out_hash[k])