import os.path
import numpy as np
import pandas as pd
from preprocess import preprocess
from myLinearSVM import linearSVM
from myKernelSVM import kernelSVM
from myMLP import MLP
from myVisualizer import visualizer
from pca import pca
from matplotlib import pyplot as plt

def main():
    ## assume if y_test exists, all csv files exist
    if not os.path.exists('y_test.csv'):
        preprocess()

    n = 600
    X_train = np.asarray(pd.read_csv("X_train.csv"))[:n]
    Y_train = np.asarray(pd.read_csv("y_train.csv"))[:n].reshape([X_train.shape[0],])
    X_test = np.asarray(pd.read_csv("X_test.csv"))
    Y_test = np.asarray(pd.read_csv("y_test.csv")).reshape([X_test.shape[0],])

    ## setup for fashion dataset
    ftrain = np.genfromtxt("fashion-mnist_train.csv", delimiter=",")[:6000]
    ftrain0 = ftrain[ftrain[:, 0] == 0]
    ftrain1 = ftrain[ftrain[:, 0] == 1]
    ftrain1 = ftrain1
    ftrain0 = ftrain0
    X_ftrain = np.concatenate((ftrain0[:, 1:], ftrain1[:, 1:]))
    Y_ftrain = np.concatenate((ftrain0[:, 0], ftrain1[:, 0]))
    ftest = np.genfromtxt("fashion-mnist_test.csv", delimiter=",")
    ftest0 = ftest[ftest[:, 0] == 0]
    ftest1 = ftest[ftest[:, 0] == 1]
    X_ftest = np.concatenate((ftest0[:, 1:], ftest1[:, 1:]))
    Y_ftest = np.concatenate((ftest0[:, 0], ftest1[:, 0]))

    X_ftrain /= 255
    X_ftest /= 255

    ## #2
    data = [X_train, Y_train, X_test, Y_test]
    fdata = [X_ftrain, Y_ftrain, X_ftest, Y_ftest]

    print("Linear SVM, Lungs: \n")
    final_C_lin, error_lin, model = linearSVM(data)
    print("Linear SVM, Fashion: \n")
    ffinal_C_lin, ferror_lin, fmodel = linearSVM(fdata)

    ## #3
    print("Kernel SVM, Lungs: \n")
    final_C_kern, error_kern, model = kernelSVM(data)
    print("Kernel SVM, Fashion: \n")
    ffinal_C_kern, ferror_kern, fmodel = kernelSVM(fdata)

    ## now compare the two for problem #4
    data_pca = pca(data)

    final_C_lin, error_lin, model = linearSVM(data_pca, final_C_lin)
    plt = visualizer(data_pca, model, "Linear SVM Visualization, PCA on Lungs", ("Negative", "Positive"))
    plt.show(block=False)

    final_C_kern, error_kern, model = kernelSVM(data_pca, final_C_kern)
    plt = visualizer(data_pca, model, "Kernel SVM Visualization, PCA on Lungs", ("Negative", "Positive"))
    plt.show(block=False)

    fdata_pca = pca(fdata)

    ffinal_C_lin, ferror_lin, fmodel = linearSVM(fdata_pca, ffinal_C_lin)
    plt = visualizer(fdata_pca, fmodel, "Linear SVM Visualization, PCA on Fashion", ("T-Shirts", "Trousers"))
    plt.show(block=False)

    ffinal_C_kern, ferror_kern, fmodel = kernelSVM(fdata_pca, ffinal_C_kern)
    plt = visualizer(fdata_pca, fmodel, "Kernel SVM Visualization, PCA on Fashion", ("T-Shirts", "Trousers"))
    plt.show(block=False)

    ## #5 multi-layer perceptron for extra credit
    final_C_mlp, error_mlp = MLP(data)
    ffinal_C_mlp, ferror_mlp = MLP(fdata)

    if error_lin < error_kern:
        print("LINEAR SVM PERFORMS BETTER WITH AN ERROR RATE OF {}".format(error_lin))
    elif error_kern < error_lin:
        print("KERNEL SVM PERFORMS BETTER WITH AN ERROR RATE OF {}".format(error_kern))
    else:
        print("BOTH PERFORM EQUALLY WITH AN ERROR RATE OF {}".format(error_lin))

    if ferror_lin < ferror_kern:
        print("LINEAR SVM PERFORMS BETTER WITH AN ERROR RATE OF {}".format(ferror_lin))
    elif ferror_kern < ferror_lin:
        print("KERNEL SVM PERFORMS BETTER WITH AN ERROR RATE OF {}".format(ferror_kern))
    else:
        print("BOTH PERFORM EQUALLY WITH AN ERROR RATE OF {}".format(ferror_lin))


if __name__ == '__main__':
    main()
