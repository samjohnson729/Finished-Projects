import numpy as np
import pandas as pd
from PIL import Image

def preprocess():
    train_file_names = pd.read_csv("train.csv")
    test_file_names = pd.read_csv("test.csv")

    Xtrain = []
    Ytrain = []
    Xtest = []

    for i,train_file in train_file_names.iterrows():
        img = np.asarray(Image.open("train/" + str(train_file["id"]) + ".png").convert('L')).reshape(28*28) / 255.
        Xtrain.append(img)
        Ytrain.append(train_file["label"])

    for i, test_file in test_file_names.iterrows():
        img = np.asarray(Image.open("test/" + str(test_file["id"]) + ".png").convert('L')).reshape(28 * 28) / 255.
        Xtest.append(img)

    Xtrain = np.asarray(Xtrain)
    Ytrain = np.asarray(Ytrain)
    Xtest = np.asarray(Xtest)
    np.savetxt("Xtrain.csv", Xtrain, delimiter=',')
    np.savetxt("Ytrain.csv", Ytrain, delimiter=',')
    np.savetxt("Xtest.csv", Xtest, delimiter=',')

if __name__=="__main__":
    preprocess()