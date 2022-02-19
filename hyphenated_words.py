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
#parser.add_argument("-o", "--output", dest="outfile",
#					help="provide outputfilename",required=False)

args = parser.parse_args()
inputfile = args.inputfile

df = pd.read_excel(inputfile, header=None, na_filter=False)
df1 = df

outfile = re.sub(r'.xlsx', '-out.xlsx', inputfile)
hyphen_words = []
for index,row in df.iterrows():
	#print(row[1])
	tgt = row[1]
	tgt = re.sub(r'( +)?-( +)?', '-', tgt)
	words = re.findall(r'[\u0900-\u09FF]+(?:-[\u0900-\u09FF]+)+', tgt)
	words = ", ".join(words)
	hyphen_words.append(words)
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