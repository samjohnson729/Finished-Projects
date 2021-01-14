import numpy as np
import pandas as pd
import os
from preprocess import *
from keras.utils import to_categorical
from keras.layers import Conv2D, Dense, MaxPool2D, Flatten, Dropout
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import *

def main():
    if not os.path.exists("Xtest.csv"):
        preprocess()

    Xtrain = np.asarray(pd.read_csv("Xtrain.csv", header=None))
    Xtrain = Xtrain.reshape([len(Xtrain), 28, 28, 1])
    Ytrain = np.asarray(pd.read_csv("Ytrain.csv", header=None))
    Ytrain = to_categorical(Ytrain.reshape(len(Ytrain)))
    Xtest = np.asarray(pd.read_csv("Xtest.csv", header=None))
    Xtest = Xtest.reshape([len(Xtest), 28, 28, 1])

    val_cutoff = round(.8 * len(Xtrain))
    xtrain = Xtrain[:val_cutoff,:]
    ytrain = Ytrain[:val_cutoff]
    xval = Xtrain[val_cutoff:,:]
    yval = Ytrain[val_cutoff:]


    model = Sequential()
    model.add(Conv2D(filters=64, kernel_size=(3,3), activation='relu', input_shape=xtrain.shape[1:]))
    model.add(Conv2D(filters=64, kernel_size=(3,3), activation='relu'))
    model.add(MaxPool2D(pool_size=(2,2)))
    model.add(Dropout(rate=.25))
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(rate=.5))
    model.add(Dense(10, activation='softmax'))

    model.compile(
        loss='categorical_crossentropy',
        optimizer='adam',
        metrics=['accuracy']
    )

    datagen = ImageDataGenerator(
        rotation_range=10,
        zoom_range=0.1,
        width_shift_range=.1,
        height_shift_range=.1
    )

    epochs = 20
    batch_size = 4
    model.fit(datagen.flow(xtrain, ytrain, batch_size=batch_size), epochs=epochs,
              validation_data=(xval, yval), steps_per_epoch=len(xtrain)//batch_size)
    test_pred = np.argmax(model.predict(Xtest), 1)

    test_ids = np.asarray(pd.read_csv("test.csv")["id"])
    submission = np.c_[test_ids, test_pred]
    submission = pd.DataFrame(submission)
    submission.to_csv("submission.csv", index=False, header=["id", "label"])


if __name__ == "__main__":
    main()
