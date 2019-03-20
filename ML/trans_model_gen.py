import pandas as pd
import numpy as np
from sklearn import linear_model
import pickle
import sys

#open file using open file mode

fp1 = open(sys.argv[1]) # Open file on read mode
lines1 = fp1.read()#.split("\n") # Create a list containing all lines
fp1.close() # Close file


fp2 = open(sys.argv[2]) # Open file on read mode
lines2 = fp2.read()#.split("\n") # Create a list containing all lines
fp1.close() # Close file


a = np.loadtxt(lines1)
b = np.loadtxt(lines2)


#creating and training a model
regr = linear_model.LinearRegression()
regr.fit(a, b)

#serializing our model to a file called model.pkl
pickle.dump(regr, open("trans_model.pkl","wb"))

#loading a model from a file called model.pkl
#model = pickle.load(open("model.pkl","r"))