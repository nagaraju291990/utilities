#resotre mongo collection one by one

import time
import subprocess
import os
import shutil
import sys

input=sys.argv[1]
backup_path="/home/nagaraju/Downloads/2019-01-25-110001/postedit-db-0-4"

with open(input) as fp:
    colls = fp.read().split("\n")

now=int(time.time())

for col_name in colls:
	cmd="mongorestore --db postedit-db-0-4 --collection " + col_name + ' ' + backup_path + "/" + col_name + '.bson'
	print (subprocess.check_output(cmd,stderr=subprocess.STDOUT,shell=True))
