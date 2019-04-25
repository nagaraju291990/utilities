'''author:Nagaraju V '''
import re
import sys
from argparse import ArgumentParser

parser = ArgumentParser(description='Ngram generator for a text file \n\r')

parser.add_argument("-i", "--input", dest="inputfile",
                    help="provide a text file",required=True)
parser.add_argument("-n", "--noofGrams",
                    dest="noofGrams", help="-n=1|2|3|4|...",required=True)

args = parser.parse_args()
inputfile = args.inputfile
noofGrams = args.noofGrams

noofGrams = int(noofGrams)

#open file using open file mode

fp1 = open(inputfile) # Open file on read mode
lines = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file

ngram_hash = {}

def generate_ngrams(s, n):
    # Convert to lowercases
    s = s.lower()
    
    # Replace all none alphanumeric characters with spaces
    #s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
    
    # Break sentence in the token, remove empty tokens
    tokens = [token for token in s.split(" ") if s != ""]
    
    ngrams = []
    # Use the zip function to help us generate n-grams
    # Concatentate the tokens into ngrams and return
    #ngrams = zip(*[tokens[i:] for i in range(n)])
    for i in range(n):
    	if(len(tokens) >=n):
    		ngrams.append(tokens[:n])
    		#print(ngrams)
    	else:
    		return
    #print(ngrams)
    for ngram in ngrams:
    	#print(ngram)
    	ngram = ' '.join(str(e) for e in ngram)
    	#print(ngram)
    	if(ngram in ngram_hash):
    		tmp = ngram_hash[ngram]
    		print(tmp)
    		ngram_hash[ngram] = tmp + 1
    	else:
    		ngram_hash[ngram] = 1
    #return [" ".join(ngram) for ngram in ngrams]

for line in lines:
	if(line != ""):
		generate_ngrams(line, noofGrams)

for key in ngram_hash:
	print(key,ngram_hash[key],"\n")
#print(ngram_hash)