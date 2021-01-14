import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
import PIL

def preprocess():
    data_shape = [28,28]
    train_test_split = .7

    files = np.asarray(list(glob.glob("chest_xray/*/*/*.jpeg")))
    np.random.shuffle(files)

    image = PIL.Image.open(files[0]).convert('L').resize(data_shape)
    image.save("test.jpeg")

    n = len(files)
    n_cutoff = round(n * train_test_split)
    
    X = np.zeros([n,data_shape[0]*data_shape[1]])
    y = np.zeros(n, dtype = np.int32)
    for i in range(n):
        x = PIL.Image.open(files[i]).convert('L')
        x = np.array(x.resize(data_shape))
        X[i] = x.reshape([x.shape[0]*x.shape[1],]).astype('float32') / 255.
        if "PNEUMONIA" in files[i]: y[i] = 1
        elif "NORMAL" in files[i]: y[i] = 0
        else: print("ERROR with file: " + str(files[i]))

    data = np.c_[X, y]
    np.random.shuffle(data)
    X_train = data[:n_cutoff,:-1]
    y_train = data[:n_cutoff,-1]
    X_test = data[n_cutoff:,:-1]
    y_test = data[n_cutoff:,-1]

    np.savetxt("X_train.csv", X_train, delimiter = ",")
    np.savetxt("y_train.csv", y_train, delimiter = ",")
    np.savetxt("X_test.csv", X_test, delimiter = ",")
    np.savetxt("y_test.csv", y_test, delimiter = ",")

    print("Sample Size: " + str(n))
    print("Train Size: " + str(n_cutoff))
    print("Test Size: " + str(n - n_cutoff))


if __name__ == '__main__':
    preprocess()
