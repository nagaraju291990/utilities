import pyonmttok
import sys

tokenizer = pyonmttok.Tokenizer("conservative", joiner_annotate=False)

with open(sys.argv[1]) as fp:
	lines = fp.read()

for line in lines.split("\n"):
	if(line == ""):
		break
	tokens = tokenizer.tokenize(line)
	#print(type(tokens))
	#print(str(tokens)[1:-1])
	#print(str(tokens[0])[1:-1])
	print(' '.join([str(i) for i in tokens[0]]))
