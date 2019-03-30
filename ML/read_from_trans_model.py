#import pandas as pd
#import numpy as np
#from sklearn import linear_model
import pickle

#loading a model from a file called model.pkl
model = pickle.load(open("trans_model.pkl","rb"))

print (model.predict([[a,l,l,i,p,u,d,i]]).tolist())