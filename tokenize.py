import nltk
import sys

with open(sys.argv[1]) as f:
	lines = f.readlines()
#sentence = """At eight o'clock on Thursday morning
#... Arthur didn't feel very good."""
for line in lines:
	sentences = nltk.tokenize.sent_tokenize(line)
	for sentence in sentences:
		print(sentence)
