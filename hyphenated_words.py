import sys
import csv
import re
import pandas as pd
from argparse import ArgumentParser

parser = ArgumentParser(description='This script will align extract hyphenated words from 2nd column of a excel input file and append in 3rd column\n\r'+
						"How to Run?\n" +
						"python3 " + sys.argv[0] + " -i=input.xlsx" 
						)
parser.add_argument("-i", "--inputfile", dest="inputfile",
					help="provide input file in xlsx",required=True)
parser.add_argument("-b", "--bagfile", dest="bagfile",
					help="provide bagfilename",required=True)

args = parser.parse_args()
inputfile = args.inputfile
bagfilename = args.bagfile

#open list file using open file mode
fp4 = open(bagfilename, encoding="utf-8") # Open file on read mode
tgtbag_words = fp4.read().split("\n") # Create a list containing all lines
fp4.close() # Close file

df = pd.read_excel(inputfile, header=None, na_filter=False)
df1 = df

tgt_bag_hash = {}
for tgt in tgtbag_words:
	if(tgt == ""):
		continue
	tgt_split = tgt.split("\t")
	tgt_bag_hash[tgt_split[1]] = '1'

outfile = re.sub(r'.xlsx', '-out.xlsx', inputfile)
file_unique_hash = {}
hyphen_words = []
for index,row in df.iterrows():
	#print(row[1])
	tgt = row[1]
	tgt = re.sub(r'( +)?-( +)?', '-', tgt)
	words = re.findall(r'[\u0900-\u09FF]+(?:-[\u0900-\u09FF]+)+', tgt)
	words = list(set(words))
	words = [re.sub(r'[\?\u0964\,\.,\[\]\;:\'\"]', '', w) for w in words if w]
	out_words = []
	for w in words:
		ww = w.split("-")
		if(ww[0] == ww[1]):
			continue
		if w in tgt_bag_hash:
			file_unique_hash[w] = 'e'
			out_words.append(w + '[e]')
		elif w in file_unique_hash:
			file_unique_hash[w] = 'd'
			out_words.append(w + ' [d]')
		else:
			file_unique_hash[w] = '1'
			out_words.append(w)
	out_words = ", ".join(out_words)
	hyphen_words.append(out_words)
	#for word in words:

data = []
#print(hyphen_words)
#print(type(df.iloc[:,0].tolist()))
col1 = df.iloc[:,0].tolist()
col2 = df.iloc[:, 1].tolist()
col3 = hyphen_words
df = pd.DataFrame(data=list(zip(col1, col2, col3)))
df = df.fillna('')
#print(type(df))
print(df)
df.to_excel(outfile, sheet_name='sheet1', index=False, header=False)

		#print(word)