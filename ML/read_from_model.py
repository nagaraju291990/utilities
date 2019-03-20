#import pandas as pd
#import numpy as np
#from sklearn import linear_model
import pickle

#loading a model from a file called model.pkl
model = pickle.load(open("model.pkl","rb"))

print (model.predict([[7.4,0.66,0,1.8,0.075,13,40,0.9978,3.51,0.56,9.4]]).tolist())