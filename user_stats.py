#program to search for input in master file, both files are assumed to be tab seperated and can have multiple columns
import sys
import re
from argparse import ArgumentParser

parser = ArgumentParser(description='To find in master file the contents of input file print into matched.txt and not matchedd.txt \n\rBoth files are tab seperated and can have multiple columns'+
						"How to Run?\n" +
						"python3 " + sys.argv[0] + " -i=inputfie"
						)

parser.add_argument("-i", "--input", dest="inputfile",
					help="provide .txt file name",required=True)
parser.add_argument("-o", "--output", dest="outfile",
					help="provide .txt file name",required=True)

args = parser.parse_args()

inputfile = args.inputfile
outfile = args.outfile

#open input file using open file mode
fp1 = open(inputfile, encoding="utf-8") # Open file on read mode
lines = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file

stats_hash = {}
for line in lines:
	if(re.search(r'TaskID', line)):
		continue
	line = re.sub(r'","', '\t', line)
	cols = line.split("\t")
	user = cols[7]
	word_count = cols[5]
	if(user in stats_hash):
		wc = stats_hash[user]
		stats_hash[user] = wc + int(word_count)
	else:
		stats_hash[user] = int(word_count)

fpw = open(outfile, "w", encoding="utf-8")

for keys in stats_hash.keys():
	fpw.write(keys + "\t" + str(stats_hash[keys]) + "\n")

fpw.close()