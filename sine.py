from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM
from keras.preprocessing.sequence import pad_sequences

from matplotlib import pyplot as plt

#sine and cos wave
import numpy as np


X = np.linspace(0,1000,10000)
Y = np.asarray([np.sin(X),np.cos(X)]).T


# data prep
# use 500 data points of historical data to predict 500 data points in the future
data = Y
examples = 500
y_examples = 500

nb_samples = len(data) - examples - y_examples


# input - 2 features
input_list = [np.expand_dims(np.atleast_2d(data[i:examples+i,:]), axis=0) for i in xrange(nb_samples)]
input_mat = np.concatenate(input_list, axis=0)

print input_mat.shape
# target - the first column in merged dataframe
target_list = [np.atleast_2d(data[i+examples:examples+i+y_examples,0]) for i in xrange(nb_samples)]
target_mat = np.concatenate(target_list, axis=0)


# set up model
trials = input_mat.shape[0]
features = input_mat.shape[2]
print trials
print features
hidden = 64
model = Sequential()

model.add(LSTM(input_dim=features, output_dim=hidden))
model.add(Dropout(.2))
model.add(Dense(input_dim=hidden, output_dim=y_examples))

model.add(Activation('linear'))
model.compile(loss='mse', optimizer='rmsprop')


# Train

model.fit(input_mat, target_mat, nb_epoch=2)
print_layer_shapes(model, input_shapes =(input_mat.shape))

