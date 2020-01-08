#script to remove tags from transcription file
from argparse import ArgumentParser
import re
import sys
from bs4 import BeautifulSoup

def striphtmlDelete(data):
	#print(data)
	data = re.sub(r'<sp>', '', data)
	data = re.sub(r'<.*?>.*?<\/.*?>','', data)
	return data
	#return p.sub('', data)


def striphtml(data):
	soup = BeautifulSoup(data,'html.parser')
	return soup.get_text()

parser = ArgumentParser(description='Remove tags from transcription file \n\r'+
						"How to Run?\n" +
						"python3 " + sys.argv[0] + " -i=inputfie" + " -f=y|n"
						)

parser.add_argument("-i", "--input", dest="inputfile",
					help="provide .txt file name",required=True)
parser.add_argument("-f", "--flag", dest="flag",
					help="specify Y|y for yes or N|n for no to include or exclude text in tags, default=yes", required=False)

args = parser.parse_args()

inputfile = args.inputfile
flag = args.flag

if(flag == None):
	flag = 'n'
else:
	flag = flag.lower()


fp = open(inputfile, "r",  encoding='utf-8')
lines = fp.read().split("\n")
fp.close()


for line in lines:
	line = re.sub(r'>', '> ', line, flags=re.MULTILINE)
	if(flag == 'y'):
		line = striphtmlDelete(line)
	else:
		line = striphtml(line)
	
	line = re.sub(r'^ *',"",line,flags=re.MULTILINE)
	line = re.sub(r' *$',"",line,flags=re.MULTILINE)
	line = re.sub(r' +', " ",line,flags=re.MULTILINE)
	print(line)
	#print(line2)