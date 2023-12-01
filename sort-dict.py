import sys

inpfile = sys.argv[1]

#open file using open file mode
fp1 = open(inpfile, "r", encoding="utf-8", errors="ignore") # Open file on read mode -- input file
lines = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file

outarr = []
for line in lines:
	line = line.strip()
	if(line == ""):
		continue
	arr = line.split(",")
	oline = []
	oline.append(arr[2])
	oline.append(arr[1])
	oline.append(arr[0])
	outarr.append(arr[2] + "," + arr[1] + "," + arr[0])
	#print(oline)

outarr.sort()
print("\n".join(outarr))