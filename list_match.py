#find and replace words from a tab seperated list into the input file
#how to run:? python3 list_match.py inputfile.txt list.txt(tab seperated)
import sys
import re

#open file using open file mode
fp1 = open(sys.argv[1]) # Open file on read mode
lines = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file


fp2 = open(sys.argv[2]) # Open file on read mode
words = fp2.read().split("\n") # Create a list containing all lines
fp2.close() # Close file

six_word_hash = {}
five_word_hash = {}
four_word_hash = {}
three_word_hash = {}
two_word_hash = {}

word_hash = {}
all_hash = {}

for word in words:
	#print(word)
	#word = word.lower()
	if(word != ""):
		tsl = word.split("\t")
		if(len(re.findall(" ", tsl[0])) == 5 ):
			six_word_hash[tsl[0]] = tsl[1]
		elif(len(re.findall(" ", tsl[0])) == 4 ):
			five_word_hash[tsl[0]] = tsl[1]
		elif(len(re.findall(" ", tsl[0])) == 3 ):
			four_word_hash[tsl[0]] = tsl[1]
		elif(len(re.findall(" ", tsl[0])) == 2 ):
			three_word_hash[tsl[0]] = tsl[1]
		elif(len(re.findall(" ", tsl[0])) == 1 ):
			two_word_hash[tsl[0]] = tsl[1]
		else:
			word_hash[tsl[0]] = tsl[1]

#print(word_hash)
for d in (six_word_hash, five_word_hash, four_word_hash, three_word_hash, two_word_hash, word_hash):
	all_hash.update(d)

#keys = word_hash.keys()
keys = all_hash.keys()
#print(keys)
#skeys = sorted(keys, key=lambda x:x.split(" "),reverse=True)
#print (skeys)

for line in lines:
	if(line != ""):
		for key in keys:
			#my_regex = key + r"\b"
			my_regex = r"([,\"\'\( \/\-\|])" + key + r"([ ,\.!\"।\'\/\-)])"
			#print(my_regex)
			if((re.search(my_regex, line, re.IGNORECASE|re.UNICODE))):
				tgt = all_hash[key]
				tgt = re.sub(r' ', "replaced###already", tgt, flags=re.IGNORECASE|re.MULTILINE)
				line = re.sub(my_regex, r"\1" + tgt +r"\2",line,flags=re.IGNORECASE|re.UNICODE|re.MULTILINE)
				#print("iam :1",line)
			if((re.search(r"([,\"\'\( \/\-])" + key + r"$", line, re.IGNORECASE|re.UNICODE))):
				tgt = all_hash[key]
				tgt = re.sub(r' ', "replaced###already", tgt, flags=re.IGNORECASE|re.MULTILINE)
				line = re.sub(key+r"$", tgt ,line,flags=re.IGNORECASE|re.UNICODE|re.MULTILINE)
				#print("iam :2",line)
			if((re.search(r"^" + key + r"([ ,\.!\"।\'\/\-)])", line, re.IGNORECASE|re.UNICODE))):
				tgt = all_hash[key]
				tgt = re.sub(r' ', "replaced###already", tgt, flags=re.IGNORECASE|re.MULTILINE)
				line = re.sub(r"^" + key, tgt, line,flags=re.IGNORECASE|re.UNICODE|re.MULTILINE)
				#print("iam :",line, key)
			if((re.search(r"^" + key + r"$", line, re.IGNORECASE|re.UNICODE))):
				#print(line)
				tgt = all_hash[key]
				tgt = re.sub(r' ', "replaced###already", tgt, flags=re.IGNORECASE|re.MULTILINE)
				line = re.sub(r"^" + key + r"$", tgt ,line,flags=re.IGNORECASE|re.UNICODE|re.MULTILINE)
				#print("iam :",line)
		line = re.sub(r'replaced###already', " ", line, flags=re.IGNORECASE|re.MULTILINE)
		print(line)
	else:
		print(line)
