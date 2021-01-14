import pandas as pd
import numpy as np
from sklearn.svm import LinearSVC, SVC

def kernelSVM(data, final_C=None):
    print("BEGIN KERNEL SVM TRAINING AND TESTING")
    n = 600 # number of training samples to use
    k = 5 # Cross validation parameter
    C = [.01, .1, 1., 10, 100]

    X_train = data[0]
    Y_train = data[1]
    X_test = data[2]
    Y_test = data[3]

    X_train = np.c_[np.arange(len(X_train)) % k, X_train]
    Y_train = np.c_[np.arange(len(Y_train)) % k, Y_train]

    if not final_C:
        print("NOW CROSS VALIDATING TO FIND OPTIMAL C")
        final_C = C[0]

        errors_train = np.ones([len(C),k])
        errors_val = np.ones([len(C),k])
        for c_ind,c in enumerate(C):
            model = SVC(kernel='rbf', C=c, gamma = 'auto', max_iter = 10000)
            for i in range(k):
                x_train = X_train[X_train[:,0] != i][:,1:]
                y_train = Y_train[Y_train[:,0] != i][:,1]
                x_val = X_train[X_train[:,0] == i][:,1:]
                y_val = Y_train[Y_train[:,0] == i][:,1]

                model.fit(x_train, y_train)

                pred_train = model.predict(x_train)
                pred_val = model.predict(x_val)

                confusion_matrix_train = np.array([[sum((y_train == 0) & (pred_train == 0)), sum((y_train == 1) & (pred_train == 0))],
                                                   [sum((y_train == 0) & (pred_train == 1)), sum((y_train == 1) & (pred_train == 1))]])
                confusion_matrix_val = np.array([[sum((y_val == 0) & (pred_val == 0)), sum((y_val == 1) & (pred_val == 0))],
                                                 [sum((y_val == 0) & (pred_val == 1)), sum((y_val == 1) & (pred_val == 1))]])
                error_train = float(sum(y_train != pred_train)) / len(y_train)
                error_val = float(sum(y_val != pred_val)) / len(y_val)
                errors_train[c_ind][i] = error_train
                errors_val[c_ind][i] = error_val

            if np.argmin(np.mean(errors_val,1)) == c_ind: final_C = c
            print("C = " + str(c))
            print("    Cross-validation train error = " + str(round(np.mean(errors_train[c_ind]),6)))
            print("    Cross-validation test error = " + str(round(np.mean(errors_val[c_ind]),6)))

    print("Optimal C parameter: C = " + str(final_C))

    model = SVC(kernel='rbf', C=final_C, gamma = 'auto', max_iter = 10000)
    model.fit(X_train[:,1:], Y_train[:,1])
    pred_train = model.predict(X_train[:,1:])
    pred_test = model.predict(X_test)

    confusion_matrix_train = np.array([[sum((Y_train[:,1] == 0) & (pred_train == 0)), sum((Y_train[:,1] == 1) & (pred_train == 0))],
                                       [sum((Y_train[:,1] == 0) & (pred_train == 1)), sum((Y_train[:,1] == 1) & (pred_train == 1))]])
    confusion_matrix_test = np.array([[sum((Y_test == 0) & (pred_test == 0)), sum((Y_test == 1) & (pred_test == 0))],
                                      [sum((Y_test == 0) & (pred_test == 1)), sum((Y_test == 1) & (pred_test == 1))]])
    error_train = float(sum(Y_train[:,1] != pred_train)) / len(Y_train[:,1])
    error_test = float(sum(Y_test != pred_test)) / len(Y_test)

    print("Testing error = " + str(error_test))
    print("Testing confusion matrix:")
    print(confusion_matrix_test)
    print()

    return final_C, error_test, model

if __name__ == '__main__':
    X_train = np.asarray(pd.read_csv("X_train.csv"))[:n]
    Y_train = np.asarray(pd.read_csv("y_train.csv"))[:n].reshape([X_train.shape[0],])
    X_test = np.asarray(pd.read_csv("X_test.csv"))
    Y_test = np.asarray(pd.read_csv("y_test.csv")).reshape([X_test.shape[0],])

    data = [X_train, Y_train, X_test, Y_test]
    kernelSVM(data)
