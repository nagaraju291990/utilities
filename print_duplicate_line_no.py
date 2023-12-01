import re
import sys

duplicate_dict = {}

with open(sys.argv[1]) as fp:
	#lines = fp.read()
    for line in fp:
        line = line.strip()
        line = re.sub(r' +', ' ', line)
        if(line in duplicate_dict):
            get_count = duplicate_dict[line]
            duplicate_dict[line] = get_count + 1
        else:
            duplicate_dict[line] = [1

for d in duplicate_dict:
    if(duplicate_dict[d] > 1):
        print(str(duplicate_dict[d]) + "\t" + d)