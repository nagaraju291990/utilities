#pip3 install pygtrie
#new dev commit
from argparse import ArgumentParser
import sys
import re
import os.path

parser = ArgumentParser(description='This script will count number of words and gives sentence number\n\r'+
						"How to Run?\n" +
						"python3 " + sys.argv[0] + " -i=inpu.txt" + " -n=[10000]"
						)
parser.add_argument("-i", "--input", dest="inputfile",
                    help="provide paradigm file name",required=True)
parser.add_argument("-n", "--number", dest="number",
                    help="provide tokens number like 10000 or 20000",required=True)

args = parser.parse_args()

inputfile = args.inputfile
number = int(args.number)

word_count = 0
sent_count = 0
file_exists = os.path.exists(inputfile)
if(not file_exists):
	print("Given %s does not exists" %(inputfile))
	exit()
else:
	isDirectory = os.path.isdir(inputfile)
	if(isDirectory):
		files = os.listdir(inputfile)
		for f in files:
			print(os.path.abspath(inputfile) + "/" + f)
			if(os.path.isfile(os.path.abspath(inputfile) +"/" +f)):
				print("Executing the file:", os.path.basename(inputfile)+"/" +f)
				with open(inputfile + "/" + f, encoding="utf8", errors='ignore') as f: # Open file on read mode -- input file
					lines = [line.rstrip() for line in f]
				#fp1.close() # Close file
				#print(lines)
				#len(lines)
				#sent_count += len(lines)
				for l in lines:
					words = l.split(" ")
					word_count += len(words)
					sent_count += 1
					#if(word_count > number):
					print("Total number of Senteces reached=%s to get %s tokens" %(sent_count, word_count))
						#exit()
	else:
		with open(inputfile,  errors='ignore') as f: # Open file on read mode -- input file
			lines = [line.rstrip() for line in f]
		#fp1.close() # Close file
		#print(lines)		
		for l in lines:
			words = l.split(" ")
			word_count += len(words)
			sent_count += 1
			if(word_count > number):
				print("Total number of Senteces reached=%s to get %s tokens" %(sent_count, number))
				exit()
