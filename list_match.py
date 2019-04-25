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

word_hash = {}

for word in words:
	#print(word)
	if(word != ""):
		tsl = word.split("\t")
		word_hash[tsl[0]] = tsl[1]

#print(word_hash)
keys = word_hash.keys()
#skeys = sorted(keys, key=lambda x:x.split(" "),reverse=True)
#print(keys)
#print (skeys)

for line in lines:
	if(line != ""):
		for key in keys:
			#my_regex = key + r"\b"
			my_regex = r"([\"\'\( \/])" + key + r"([ ,\.!\"।\'\/)])"
			#print(my_regex)
			if((re.search(my_regex, line, re.IGNORECASE|re.UNICODE))):
				line = re.sub(my_regex, r"\1" + word_hash[key]+r"\2",line,flags=re.IGNORECASE|re.UNICODE|re.MULTILINE)
				#print("iam :1",line)
			if((re.search(key + r"$", line, re.IGNORECASE|re.UNICODE))):
				line = re.sub(key+r"$", word_hash[key],line,flags=re.IGNORECASE|re.UNICODE|re.MULTILINE)
				#print("iam :2",line)
			if((re.search(r"^" + key, line, re.IGNORECASE|re.UNICODE))):
				#print(line)
				line = re.sub(r"^" + key, word_hash[key],line,flags=re.IGNORECASE|re.UNICODE|re.MULTILINE)
				#print("iam :",line)
		print(line)
	else:
		print(line)
