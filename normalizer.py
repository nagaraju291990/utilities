import re
import sys

with open(sys.argv[1]) as fp:
	lines = fp.read()

#lines = re.sub(r'\n\n\n\n', "\n", lines, flags=re.MULTILINE)
#lines = re.sub(r'\n\n\n', "\n", lines, flags=re.MULTILINE)
#lines = re.sub(r'\n\n', "\n", lines, flags=re.MULTILINE)

for line in lines.split("\n"):
	#line = line.lower() #convert to lowercase

	line = re.sub(r'\uFFFD', "-", line, flags = re.MULTILINE) #replacement character
	line = re.sub(r'\u000C', "", line, flags = re.MULTILINE)	#formfeed
	line = re.sub(r'\u00A0'," ", line, flags = re.MULTILINE)    #convert nbsp space to normal space
	line = re.sub(r'\t', " ", line, flags = re.MULTILINE)     #tab to space
	line = re.sub(r'^ *',"", line, flags = re.MULTILINE)
	line = re.sub(r' *$',"", line, flags = re.MULTILINE)
	line = re.sub(r' +', " ", line, flags = re.MULTILINE)
	line = re.sub(r'\n', "", line, flags = re.MULTILINE)

	line = re.sub(r'^-?\d+ ?\.?(\d+)?$', "", line, flags = re.MULTILINE) #2.3, -2.3, 23, -786
	line = re.sub(r'^\d+ ?\.? ?$', "", line, flags = re.MULTILINE)	#2
	line = re.sub(r'^([\+\-]?\d+,? ?)+$', "", line, flags = re.MULTILINE)#-6 -5 -4 -3 -2 -1, 0 +1 +2 +3 +4 +5 +6 +7
	line = re.sub(r'^\d+ ?\+ ?\d+ ?= ?\(?[\+\-]?\d+\)? ?\+ ?\(?[\+\-]?\d+\)? ?=? ?[+-]?\d+$', "", line, flags = re.MULTILINE)	#1 + 5 = (+1) + (+5) = +6
	line = re.sub(r'^=? ?\(?[\+\-]? ?\(?[\+\-]? ?\d+\)?\)? ?[\+\-\=]? ?\(?[\+\-]? ?\(?[\+\-]? ?\d+\)?\)?', "", line, flags = re.MULTILINE)#(-4) - (-9),= (-4) + 9,= -4 + 9
	line = re.sub(r'^\d+? ?[×÷] ?\d+? ?=? ?\d+?$', "", line, flags =re.MULTILINE) #6*÷2=12
	#line = re.sub(r'^ ?= ?\d+$')

	line = re.sub(r'^[A-z]$', "", line, flags = re.MULTILINE)



	line = line.lstrip()
	if(line != ""):
		print(line)
	#print(line)
