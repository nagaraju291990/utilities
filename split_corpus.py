import re
import sys

given_file = sys.argv[1]
size = int(sys.argv[2])

fp1 = open(given_file,'r')
lines = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file


lines2 = lines[0:size]

train_size = int(size * 0.8)
val_size = int(size * 0.2)

train_data = lines2[0:train_size]
val_data = lines2[train_size:]
#print(train_data)
#print(val_data)

fp2 = open("train.txt", "w")
fp2.write("\n".join(train_data))

fp3 = open("val.txt", "w")
fp3.write("\n".join(val_data))

fp2.close()
fp3.close()