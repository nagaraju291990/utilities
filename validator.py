import re
import sys

with open(sys.argv[1]) as fp:
	lines = fp.read()

line_no = 0
for line in lines.split("\n"):
	line_no += 1
	if(line == ""):
		break
	patterns = re.findall("(\(\(.*?\)\))", line)
	for m in patterns:
		pipes = len(re.findall("\|", m))
		#print(m, pipes)
		if(pipes == 2):
			tokens = re.findall("\(\((.*)\|(.*)\|(.*)?\)\)", m)
			#print("Line no:%s, tokens:%s" %(line_no,tokens))
			for i in tokens:
				if(i[1] == "" or i[2] == ""):
					print("Line no:%s token missing at:%s" %(line_no, m))
				elif(re.search("[A-z]",i[0]) or re.search("[A-z]",i[1])):
					print("Line no:%s T1 or T2 has Roman text at:%s" %(line_no, m))
		else:
			print("Line no:%s pipe count mismatch at :%s" %(line_no, m))
		