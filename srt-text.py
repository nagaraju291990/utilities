from argparse import ArgumentParser
import re
import os
import sys
import pysrt

parser = ArgumentParser(description='Extract text from srt file \n\r'+
						"How to Run?\n" +
						"python3 " + sys.argv[0] + " -i=file.srt " + "-o=all"
						)
parser.add_argument("-i", "--input", dest="inputfile",
                    help="provide .srt file name",required=True)
args = parser.parse_args()

inputfile = args.inputfile
new_line = []
timeline = []

def extractText(i):

	srtfilename = i
	subs = pysrt.open(srtfilename)
	ts_start = []
	ts_end = []
	remaining_text = ''
	front_text = ''
	#print(subs)

	for sub in subs:
		timeline_start = str(sub.start)
		timeline_end = str(sub.end)
		cur_text = sub.text
		cur_text = re.sub(r'\n', ' ' ,cur_text)
		"""
		cur_text = remaining_text + " " + str(sub.text)
		if(re.search(r'(.*)\.(.*)',cur_text)):
			m = re.search(r'(.*)\.(.*)',cur_text)
			front_text = m.group(1)
			remaining_text = m.group(2)
		else:
			front_text = cur_text
			remaining_text = ''
		#print("iam ", remaining_text)
		"""
		if(len(new_line) == 0):
			timeline.append(str(sub.start) + " --> " + str(sub.end))
			#timeline[-1] = timeline[-1].strip() + " --> " + str(sub.end)
			new_line.append(cur_text)
		elif( not re.search(r'[\.?:\-]$',new_line[-1]) and not re.search(r'^[A-Z]',cur_text)):
			timeline[-1] = timeline[-1].strip() + " --> " + str(sub.end)
			#print("Iam",cur_text)
			new_line[-1] = new_line[-1].strip() + ' ' + cur_text
		else:
			timeline.append(str(sub.start) + " --> " + str(sub.end))
			new_line.append(cur_text)
		timeline[-1] = re.sub('-->.*-->','-->',timeline[-1])
		#print(subs.text)
	#print("Subtitle processed Successfully!")



extractText(inputfile)
count = 0
for line in new_line:
	print(timeline[count])
	#if(not re.search(r'\.\.\.',line)):
	line = re.sub(r'\.', '.\n',line)
	line = re.sub(r'\n ', '\n' ,line)
	print(line)
	count = count + 1