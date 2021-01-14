import numpy as np
import pandas as pd
from preprocess import *
import os.path
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
import csv

## import the data
Xtrain = np.asarray(pd.read_csv("Xtrain.csv", header=None))[:]
Ytrain = np.asarray(pd.read_csv("ytrain.csv", header=None))[:]
Xtest = np.asarray(pd.read_csv("Xtest.csv", header=None))

## prepend the validation splitting number
Xtrain = np.c_[np.arange(len(Xtrain))%5, Xtrain]
Ytrain = np.c_[np.arange(len(Ytrain))%5, Ytrain]

params = [[100],[200,300,200],[400,500,400],[1000]]
final_param = params[0]
final_score = 0
for param in params:
    model = MLPClassifier(hidden_layer_sizes = param, activation = 'logistic', verbose=False)
    validation_scores, training_scores = [],[]
    for k in range(5):
        xtrain = Xtrain[Xtrain[:,0]!=k][:,1:]
        ytrain = Ytrain[Ytrain[:,0]!=k][:,1]
        ytrain = ytrain.reshape(len(ytrain))
        xval = Xtrain[Xtrain[:,0]==k][:,1:]
        yval = Ytrain[Ytrain[:,0]==k][:,1]
        yval = yval.reshape(len(yval))

        model.fit(xtrain, ytrain)
        train_pred = model.predict(xtrain)
        val_pred = model.predict(xval)
        print("Validation score: " + str(accuracy_score(yval, val_pred)))
        training_scores.append(accuracy_score(ytrain, train_pred))
        validation_scores.append(accuracy_score(yval, val_pred))

    print("Model parameters: " + str(param))
    print("Average training set accuracy: " + str(np.mean(training_scores)))
    print("Average validation set accuracy: " + str(np.mean(validation_scores)))
    if final_score < np.mean(validation_scores):
        final_score = np.mean(validation_scores)
        final_param = param

model = MLPClassifier(hidden_layer_sizes = final_param, activation = 'logistic', verbose=True)
model.fit(Xtrain[:,1:],Ytrain[:,1])
train_pred = model.predict(Xtrain[:,1:])
test_pred = model.predict(Xtest)

print("Final training accuracy: " + str(accuracy_score(Ytrain[:,1], train_pred)))

test = np.asarray(pd.read_csv("test.csv")["filename"])
output = []#np.empty([len(test),2])
for i,t in enumerate(test):
    output.append([t, test_pred[i]])

with open("output.csv", 'w') as f:
    write = csv.writer(f)
    write.writerow(["filename","label"])
    write.writerows(output)
