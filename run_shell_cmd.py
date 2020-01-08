"""
output directory will be created with all standard out text files
to run python3 run_shell_cmd.py <input_directory> <output_directory>
"""

import os
import sys
import subprocess
import re
from os import listdir

#from os.path import isfile, join
#from colorama import *
input_dir = sys.argv[1]
output_dir = sys.argv[2]#'out' + input_dir

srcfiles = [f for f in os.listdir(input_dir) if os.path.isfile(input_dir + '/' + f)]
srcfiles.sort()

command = 'wc -l '
"""curl -T <INPUT FILE> http://localhost:9998/tika"""
subprocess.run(["mkdir",output_dir])
for f in srcfiles:
	if(re.search(r'.*',f)):
		print("Currently running " + f)
		filename = f
		fp = open(output_dir + "/" + filename,"w")
		proc = subprocess.run(["wc", "-l", input_dir + '/' + f], encoding='utf-8', stdout=subprocess.PIPE)
		for line in proc.stdout.split('\n'):
			#print("Iam",line)
			fp.write(line+"\n")
		fp.close()
