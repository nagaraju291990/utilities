"""
This script creates a srt file
input is of following type
0:28
Hello friends, today we are looking to finish the tenth module of our course, where we are
0:33
talking about the biological effect of radiation.
0:37
"""

import sys
import re

filename = sys.argv[1]

fp = open(filename) # Open file on read mode
lines = fp.read().split("\n") # Create a list containing all lines
fp.close() # Close file

#fp2 = open("outfile.srt","w")
outfile = re.sub(r'.txt', '.srt', filename)
fp2 = open(outfile,"w")
i=0;
count = 1
for line in lines:

	if(re.search(r':\d\d$', line)):
		fp2.write(str(count) + "\n")
		count = count + 1
		time = "0:" + lines[i] + ",000 --> 0:" + lines[i+2] + ",000"
		fp2.write(time + "\n")
	else:
		fp2.write(line + "\n\n")
	i = i+1

