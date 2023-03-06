import re
import sys

inputfile = sys.argv[1]
#open file using open file mode
fp1 = open(inputfile) # Open file on read mode -- input file
lines = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file

hd = {}
for line in lines:
	if(line != ""):
		line = re.sub(r'^ *',"", line, flags = re.MULTILINE)
		line = re.sub(r' *$',"", line, flags = re.MULTILINE)
		line = re.sub(r' +', " ", line, flags = re.MULTILINE)
		hd[line] = 1
		#print(line)

for k in hd.keys():
	print(k)