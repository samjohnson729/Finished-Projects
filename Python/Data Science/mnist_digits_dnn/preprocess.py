import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd

def preprocess():

    train = pd.read_csv("train.csv")
    test = pd.read_csv("test.csv")
    
    train_files = np.asarray(train["filename"])
    train_labels = np.asarray(train["label"])
    test_files = np.asarray(test["filename"])

    ntrain = len(train_files)
    ntest = len(test_files)

    Xtrain = np.empty([ntrain, 28*28])
    ytrain = np.empty(ntrain)
    for i, f in enumerate(train_files):
        img = np.asarray(Image.open("Images/train/" + f).convert("L")).reshape(28*28)
        Xtrain[i] = img
        ytrain[i] = train_labels[i]

    Xtest = np.empty([ntest, 28*28])
    print(len(Xtest))
    for i, f in enumerate(test_files):
        img = np.asarray(Image.open("Images/test/" + f).convert("L")).reshape(28*28)
        Xtest[i] = img

    print(len(Xtest))
    print(Xtest[0])
    print(Xtest[-1])
    np.savetxt("Xtrain.csv", Xtrain, delimiter=',')
    np.savetxt("ytrain.csv", ytrain, delimiter=',')
    np.savetxt("Xtest.csv", Xtest, delimiter=',')

if __name__ == "__main__":
    preprocess()
