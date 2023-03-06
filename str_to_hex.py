import codecs
import sys

x='राम बाजार जा रहा हैं।'

fp = open(sys.argv[1], "r", encoding="utf-8")
lines = fp.read().split("\n")
fp.close()
#bx=codecs.encode(x,'utf-8')
#print("bx:",bx)
for line in lines:
	if(line == ""):
		continue
	words = line.split(" ")
	bx = codecs.encode(line, 'utf-8')
	hx=codecs.encode(bx,'hex')
	print("unicode of "+line+" is:", hx)
 