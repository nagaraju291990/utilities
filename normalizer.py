import re
import sys

with open(sys.argv[1]) as fp:
    lines = fp.read()



lines = re.sub(r'\n\n\n\n', "\n", lines, flags=re.MULTILINE)
lines = re.sub(r'\n\n\n', "\n", lines, flags=re.MULTILINE)
lines = re.sub(r'\n\n', "\n", lines, flags=re.MULTILINE)

for line in lines.split("\n"):
    #line = line.lower() #convert to lowercase
    line = re.sub(r'\u00A0'," ",line,flags=re.MULTILINE)
    line = re.sub(r'\t', "", line, flags=re.MULTILINE)
    line = re.sub(r'^ *',"",line,flags=re.MULTILINE)
    line = re.sub(r' *$',"",line,flags=re.MULTILINE)
    line = re.sub(r' +', " ",line,flags=re.MULTILINE)


    line = line.lstrip()
    if(line != ""):
        print(line)
    #print(line)