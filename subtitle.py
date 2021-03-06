#!/usr/bin/env python3

#Processing a srt file for subtitle text extraction
#pip3 install pysrt
#this will produce four output files (placeholder, new lines, without new lines, story mode)

from argparse import ArgumentParser
import os
import sys
import pysrt

parser = ArgumentParser(description='Extract text from srt file \n\r'+
						"How to Run?\n" +
						"python3 " + sys.argv[0] + " -i=file.srt " + "-o=all"
						)
parser.add_argument("-i", "--input", dest="inputfile",
                    help="provide .srt file name",required=True)
parser.add_argument("-t", "--timeline",
                    dest="timeline", help="t=yes",required=False)
parser.add_argument("-o", "--output_type",
                    dest="output_type", help="output type=1|2|3|4|ALL",required=False)

#parser.add_argument("-details" "--details",
#                                       dest="detail", help ="Optional-Value is yes or no, default is no")

args = parser.parse_args()

inputfile = args.inputfile
t = args.timeline
if(t is not None):
	t = t.lower()
output_type = args.output_type
if(output_type is not None):
	output_type = output_type.lower()
else:
	output_type = '1'

#extract sentences
def extractText(i):

	srtfilename = i
	subs = pysrt.open(srtfilename)
	#print(subs)
	#exit()
	if(output_type == "1" or output_type == "all"):
		out_file1 = open('output_file1'+os.path.basename(srtfilename),"w")
	if(output_type == "2" or output_type == "all"):
		out_file2 = open('output_file2'+os.path.basename(srtfilename),"w")
	if(output_type == "3" or output_type == "all"):
		out_file3 = open('output_file3'+os.path.basename(srtfilename),"w")
	if(output_type == "4" or output_type == "all"):
		out_file4 = open('output_file4'+os.path.basename(srtfilename),"w")
	if(t == "yes"):
		timeline_file = open('timeline_'+os.path.basename(srtfilename),"w")
	c = 1
	#print(subs)
	for sub in subs:
		if(output_type == "1" or output_type == "all"):
				out_file1.write("[SUBTITLE-"+str(c)+"]\n" + sub.text+"\n") #with placeholder
		if(output_type == "2" or output_type == "all"):
				out_file2.write("\n" + sub.text+"\n")	#with new lines
		if(output_type == "3" or output_type == "all"):
				out_file3.write(sub.text + "\n")	#without new lines  and placeholder
		if(output_type == "4" or output_type == "all"):
				out_file4.write(sub.text + " ")	#story mode
		if(t == "yes"):
				#timeline_file.write("[SUBTITLE-"+str(c)+"]\n" + str(sub.start)+ " --> " + str(sub.end)+"\n") #with placeholder
				timeline_file.write( str(sub.start)+ " --> " + str(sub.end)+"\n") #with placeholder
		c = c + 1
		#print(subs.text)
	print("Subtitle processed Successfully!")


extractText(inputfile)