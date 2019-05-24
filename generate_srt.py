#!/usr/bin/env python3

#Generate a srt file using lang file and timeline file
#pip3 install pysrt
#this will produce four output files (placeholder, new lines, without new lines, story mode)

from argparse import ArgumentParser
import os
import sys
import pysrt
import re

parser = ArgumentParser(description='Generate srt from lang file and timeline file \n\r'+
						"How to Run?\n" +
						"python3 " + sys.argv[0] + " -i=lang.txt " + "-t=timeline.txt"
						)
parser.add_argument("-i", "--input", dest="inputfile",
	help="provide .txt lang file name",required=True)
parser.add_argument("-t", "--timeline", 
	dest="timeline", help="t=timeline file",required=True)
#parser.add_argument("-details" "--details",
#                                       dest="detail", help ="Optional-Value is yes or no, default is no")

args = parser.parse_args()

inputfile = args.inputfile
timeline = args.timeline
#generate srt from timeline and lang file
def generateSRT(i, t):

	langfilename = i
	timelinefile = t

	langfp = open(langfilename,"r")
	tlfp = open(timelinefile,"r")
	outfp = open("outfile","w")

	langcontent = langfp.readlines()
	tlcontent = tlfp.readlines()
	tl_hash = {}

	count = 1
	for tls in tlcontent:
		tl_hash["SUB____" + str(count)] = tls
		count = count + 1

	lang_iterator = 0
	out = []
	for l in langcontent:
		#outfp.write(str(tl_iterator+1)+"\n")
		#outfp.write(tlcontent[tl_iterator])
		#m = re.search(r'[SUB____(\d+)',l)
		#l = l.strip()
		l = re.sub(r'\.\n','. ',l)
		l = re.sub(r"\[SUB____(\d+)\] ", r"\n[SUB____\1]\n", l, re.MULTILINE)
		#l = l.strip()
		out.append(l)
		#print (l)
	out1 = "\n".join(out)
	out = out1.split("\n")
	#print(out)
	count = 0
	fout = []
	fl = 0
	for o in out:
		#print(o,fl)
		#fl = 0
		fout.append(count + 1)
		#outfp.write(str(count + 1)+"\n")
		if(re.search(r'^\[SUB__', o)):
			fl = 0
			outfp.write("\n\n"+str(count + 1)+"\n")
			outfp.write(tlcontent[count])
			count = count + 1
		else:
			o1 = o.split(" ")
			al = len(o1)
			"""
			if(al > 8 and fl == 0):
				fl = 1 
				#o = re.sub(r'(.* ){7}',r'\1\n',o)
				o = ' '.join(o1[:7]) + "\n" + ' '.join(o1[7:])
				o = re.sub(r' $','',o)
				outfp.write(o)
			else:
				o = re.sub(r' $','',o)"""
			outfp.write(o)
			#outfp.write("\n")
			#fout.append(o)

	#outfp.write(str(fout)+"\n")
	print("Subtitle generated Successfully!")


generateSRT(inputfile,timeline)
