import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential

from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from keras.datasets import mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape (60000, 784).astype('float32') / 255
X_test = X_test.reshape (10000, 784).astype('float32') / 255

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

