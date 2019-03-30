import pandas as pd
import numpy as np
from sklearn import linear_model
import pickle

#loading and separating our wine dataset into labels and features
df = pd.read_csv('winequality-red.csv', delimiter=";")
label = df['quality']
features = df.drop('quality', axis=1)

#creating and training a model
regr = linear_model.LinearRegression()
regr.fit(features, label)

#serializing our model to a file called model.pkl
pickle.dump(regr, open("model.pkl","wb"))

#loading a model from a file called model.pkl
#model = pickle.load(open("model.pkl","r"))