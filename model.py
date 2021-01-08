#Backend Model using wind turbine dataset
# Ref: 
# 1: https://medium.com/@dvelsner/deploying-a-simple-machine-learning-model-in-a-modern-web-application-flask-angular-docker-a657db075280
# 2: https://www.analyticsvidhya.com/blog/2020/09/integrating-machine-learning-into-web-applications-with-flask/

# Import required libraries:
import tensorflow.keras as kr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn as sk
import pickle

# Import necessary modules
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
#from sklearn.datasets import make_r

#read in dataset
df = pd.read_csv("https://raw.githubusercontent.com/ClaireGMIT/MLS_Project2020/main/powerproduction.csv") 

X = df['speed']
y = df['power']

#Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

#Best fit straight line
X_avg = np.mean(X)
y_avg = np.mean(y)

X_zero = X - X_avg
y_zero = y - y_avg

m = np.sum(X_zero * y_zero)/(np.sum(X_zero * X_zero))
c = y_avg - m * X_avg

# use lambda notion: https://www.w3schools.com/python/python_lambda.asp

# Simple linear equation.
f = lambda x: m * X + c

# Create a neural network with one neuron.
model = kr.models.Sequential()
model.add(kr.layers.Dense(1, input_shape=(1,), activation="linear", kernel_initializer='ones', bias_initializer='zeros'))
model.compile('adam', loss='mean_squared_error')
model.fit(X_train, y_train, epochs=500)
model.predict([10.0,15.0,20.0,25.0])
model.evaluate(X_test, y_test)
model.fit(X, y)

# Saving model to current directory
# Pickle serializes objects so they can be saved to a file, and loaded in a program again later on.
pickle.dump(model, open('model.pkl','wb'))

#Loading model to compare the results
model1 = pickle.load(open('model.pkl','rb'))
print(model1.predict([[5.0, 15.0, 20.0]]))

