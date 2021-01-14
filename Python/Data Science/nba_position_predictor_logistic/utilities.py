import numpy as np

def train_test_split(training_percentage, data):
    data = np.asarray(data)
    np.random.shuffle(data)
    Xdata = data[:,0:-1]
    ydata = data[:,-1]

    num_train = round(len(data) * training_percentage)
    num_test = len(data) - num_train

    return Xdata[:num_train], ydata[:num_train], Xdata[num_train:], ydata[num_train:]


def isMax(x, X):
    for i in range(len(X)):
        if X[i] > x: return False
    return True
