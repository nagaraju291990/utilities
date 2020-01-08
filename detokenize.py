import pyonmttok
import sys

tokenizer = pyonmttok.Tokenizer("conservative", joiner_annotate=False)

with open(sys.argv[1]) as fp:
	lines = fp.read()

for line in lines.split("\n"):
	if(line == ""):
		break
	tokens = line.split(" ")
	#print(tokens)
	dtokens = tokenizer.detokenize(tokens)
	#print(type(dtokens))
	print(dtokens)