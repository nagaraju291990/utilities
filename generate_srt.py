#!/usr/bin/env python3

#Generate a srt file using lang file and timeline file
#pip3 install pysrt
#this will produce four output files (placeholder, new lines, without new lines, story mode)

from argparse import ArgumentParser
import os
import sys
import pysrt

parser = ArgumentParser(description='Generate srt from lang file and timeline file \n\r'+
						"How to Run?\n" +
						"python3 " + sys.argv[0] + " -i=lang.txt " + "-t=timeline.txt"
						)
parser.add_argument("-i", "--input", dest="inputfile",
                    help="provide .srt file name",required=True)
parser.add_argument("-t", "--timeline",
                    dest="timeline", help="t=yes",required=True)
parser.add_argument("-n", "--nooflines",
                    dest="n", help="n=1|2|3",required=False)
#parser.add_argument("-details" "--details",
#                                       dest="detail", help ="Optional-Value is yes or no, default is no")

args = parser.parse_args()

inputfile = args.inputfile
timeline = args.timeline
n = args.n
if(n is None):
	n = 1
else:
	n = int(n)
#generate srt from timeline and lang file
def generateSRT(i,t):

	srtfilename = i
	timelinefile = t

	srtfp = open(srtfilename,"r")
	tlfp = open(timelinefile,"r")
	outfp = open("outfile","w")

	srtcontent = srtfp.readlines()
	tlcontent = tlfp.readlines()
	srtlen = len(srtcontent)
	tllen = len(tlcontent)

	#print(n)
	tl_iterator = 0
	lang_iterator = 0
	for i in range(tllen):
		outfp.write(str(tl_iterator+1)+"\n")
		outfp.write(tlcontent[tl_iterator])
		for j in range(n):
			#print(j)
			try:	#to handle list index out of range error
				srtcontent[lang_iterator]
			except:
				break
			outfp.write(srtcontent[lang_iterator])
			lang_iterator = lang_iterator + 1
		outfp.write("\n")
		tl_iterator = tl_iterator + 1
	print("Subtitle generated Successfully!")


generateSRT(inputfile,timeline)