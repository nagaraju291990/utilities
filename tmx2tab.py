import sys
from translate.storage.tmx import tmxfile

with open(sys.argv[1], 'rb') as fin:
	tmx_file = tmxfile(fin, 'en', 'te')

for node in tmx_file.unit_iter():
	print(node.getsource(), "\t",node.gettarget())
