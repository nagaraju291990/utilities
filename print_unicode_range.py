#print_unicode_range.py F020 F0FE
import sys

start_range = sys.argv[1]
end_range = sys.argv[2]

for i in range(int(start_range,16), int(end_range,16)):
	hex2 = hex(i)
	#print( i, chr(i))#unichr(i))   ##for version2
	print(hex2, chr(i),sep="\t")
