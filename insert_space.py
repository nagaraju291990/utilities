from argparse import ArgumentParser
import re
import os
import sys

parser = ArgumentParser(description='This script will insert space when a character is capital and then the following is lower case\n\r'+
						"How to Run?\n" +
						"python3 " + sys.argv[0] + " -i=input.txt"
						)
parser.add_argument("-i", "--input", dest="inputfile",
                    help="provide .txt file name",required=True)


args = parser.parse_args()

inputfile = args.inputfile

#open file using open file mode
fp1 = open(inputfile, "r", encoding='utf-8') # Open file on read mode -- input file
lines = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file

for line in lines:
	line = re.sub(r'([a-z])([A-Z])', r'\1 \2', line)
	print(line)