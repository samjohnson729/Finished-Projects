import numpy as np
import pandas as pd
from PIL import Image
import os
from keras.datasets import mnist
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Dense, Flatten, Dropout
from sklearn.metrics import *

(Xtrain, Ytrain), (Xtest, Ytest) = mnist.load_data()
Xtrain = np.asarray(Xtrain, dtype=np.float).reshape(Xtrain.shape[0],28,28,1) / 255.
Xtest = np.asarray(Xtest, dtype=np.float).reshape(Xtest.shape[0],28,28,1) / 255.
Ytrain = to_categorical(Ytrain)
Ytest = to_categorical(Ytest)

model = Sequential()
model.add(Conv2D(filters=32, kernel_size=(5,5), activation='relu', input_shape=Xtrain.shape[1:]))
model.add(Conv2D(filters=32, kernel_size=(5,5), activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Dropout(rate=.25))
#
model.add(Flatten())
#
model.add(Dense(10, activation='softmax'))

model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

epochs = 5
batch_size = 32
history = model.fit(Xtrain, Ytrain, epochs=epochs)#, validation_data=(Xtest, Ytest))

test_pred = np.argmax(model.predict(Xtest),1)
Ytest = np.argmax(Ytest,1)
print(confusion_matrix(Ytest, test_pred))
print(accuracy_score(Ytest, test_pred))