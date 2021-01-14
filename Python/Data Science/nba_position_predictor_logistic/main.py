import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from utilities import *
from classifier import *

## READ IN THE DATA
data = pd.read_csv("seasons_stats.csv")
print(data.columns)

## USER INPUT / ARGUMENTS
input_stats = ["AST", "TRB", "STL", "BLK"]
years_range = [1975, 2017]
k = 5
d = len(input_stats)

## PRE-PROCESS THE DATA
data = data[data["Year"] >= years_range[0]]
data = data[data["Year"] <= years_range[1]]
data = data[data["MP"] > 1000]
data = data[data["Pos"]  != "G-F"]
data = data[data["Pos"]  != "F"]
data = data[data["Pos"]  != "G"]
data = data[data["Pos"]  != "F-G"]
data = data[data["Pos"]  != "F-C"]
data = data[data["Pos"]  != "C-F"]
data = data[data["Pos"]  != None]
data = data[data["Pos"]  != "PF-C"]
data = data[data["Pos"]  != "SF-SG"]
data = data[data["Pos"]  != "C-PF"]
data = data[data["Pos"]  != "SG-SF"]
data = data[data["Pos"]  != "PF-SF"]
data = data[data["Pos"]  != "SF-PF"]
data = data[data["Pos"]  != "SG-PG"]
data = data[data["Pos"]  != "SF-PG"]
data = data[data["Pos"]  != "C-SF"]
data = data[data["Pos"]  != "PG-SF"]
data = data[data["Pos"]  != "PG-SG"]
data = data[data["Pos"]  != "SG-PF"]
data["Pos"][data["Pos"] == "PG"] = 1
data["Pos"][data["Pos"] == "SG"] = 2
data["Pos"][data["Pos"] == "SF"] = 3
data["Pos"][data["Pos"] == "PF"] = 4
data["Pos"][data["Pos"] == "C"] = 5
#print(data.head())
data = data[input_stats + ["Pos"]]

## SPLIT THE DATA
Xtrain, ytrain, Xtest, ytest = train_test_split(.75, data)
print("Total samples: " + str(len(data)))
print("Train samples: " + str(len(Xtrain)))
print("Test samples: " + str(len(Xtest)))

## PRE-PROCESS THE LABEL FOR ONE-HOT ENCODING
encoded_ytrain = np.empty([len(ytrain), k])
for i in range(len(ytrain)):
    if ytrain[i] == 1: encoded_ytrain[i] = [1,0,0,0,0]
    if ytrain[i] == 2: encoded_ytrain[i] = [0,1,0,0,0]
    if ytrain[i] == 3: encoded_ytrain[i] = [0,0,1,0,0]
    if ytrain[i] == 4: encoded_ytrain[i] = [0,0,0,1,0]
    if ytrain[i] == 5: encoded_ytrain[i] = [0,0,0,0,1]

encoded_ytest = np.empty([len(ytest), k])
for i in range(len(ytest)):
    if ytest[i] == 1: encoded_ytest[i] = [1,0,0,0,0]
    if ytest[i] == 2: encoded_ytest[i] = [0,1,0,0,0]
    if ytest[i] == 3: encoded_ytest[i] = [0,0,1,0,0]
    if ytest[i] == 4: encoded_ytest[i] = [0,0,0,1,0]
    if ytest[i] == 5: encoded_ytest[i] = [0,0,0,0,1]

clf = Classify(d = d, k = k, lr = 1e-6, max_epoch = 100)

clf.fit(Xtrain, encoded_ytrain)

predictions_train = clf.predict(Xtrain)
predictions_test = clf.predict(Xtest)

## POST-PROCESS Y-VALUES TO UNDO THE ONE-HOT ENCODING
temp = np.empty(len(predictions_train))
for i in range(len(predictions_train)):
    for class_num in range(k):
        if isMax(predictions_train[i][class_num], predictions_train[i]): temp[i] = class_num + 1
predictions_train = temp
temp = np.empty(len(predictions_test))
for i in range(len(predictions_test)):
    for class_num in range(k):
        if isMax(predictions_test[i][class_num], predictions_test[i]): temp[i] = class_num + 1
predictions_test = temp



train_confusion = [[sum((ytrain==1) & (predictions_train==1)),
                    sum((ytrain==1) & (predictions_train==2)),
                    sum((ytrain==1) & (predictions_train==3)),
                    sum((ytrain==1) & (predictions_train==4)),
                    sum((ytrain==1) & (predictions_train==5))],
                   
                   [sum((ytrain==2) & (predictions_train==1)),
                    sum((ytrain==2) & (predictions_train==2)),
                    sum((ytrain==2) & (predictions_train==3)),
                    sum((ytrain==2) & (predictions_train==4)),
                    sum((ytrain==2) & (predictions_train==5))],
                   
                   [sum((ytrain==3) & (predictions_train==1)),
                    sum((ytrain==3) & (predictions_train==2)),
                    sum((ytrain==3) & (predictions_train==3)),
                    sum((ytrain==3) & (predictions_train==4)),
                    sum((ytrain==3) & (predictions_train==5))],
                   
                   [sum((ytrain==4) & (predictions_train==1)),
                    sum((ytrain==4) & (predictions_train==2)),
                    sum((ytrain==4) & (predictions_train==3)),
                    sum((ytrain==4) & (predictions_train==4)),
                    sum((ytrain==4) & (predictions_train==5))],
                   
                   [sum((ytrain==5) & (predictions_train==1)),
                    sum((ytrain==5) & (predictions_train==2)),
                    sum((ytrain==5) & (predictions_train==3)),
                    sum((ytrain==5) & (predictions_train==4)),
                    sum((ytrain==5) & (predictions_train==5))]]

test_confusion = [[sum((ytest==1) & (predictions_test==1)),
                    sum((ytest==1) & (predictions_test==2)),
                    sum((ytest==1) & (predictions_test==3)),
                    sum((ytest==1) & (predictions_test==4)),
                    sum((ytest==1) & (predictions_test==5))],
                   
                   [sum((ytest==2) & (predictions_test==1)),
                    sum((ytest==2) & (predictions_test==2)),
                    sum((ytest==2) & (predictions_test==3)),
                    sum((ytest==2) & (predictions_test==4)),
                    sum((ytest==2) & (predictions_test==5))],
                   
                   [sum((ytest==3) & (predictions_test==1)),
                    sum((ytest==3) & (predictions_test==2)),
                    sum((ytest==3) & (predictions_test==3)),
                    sum((ytest==3) & (predictions_test==4)),
                    sum((ytest==3) & (predictions_test==5))],
                   
                   [sum((ytest==4) & (predictions_test==1)),
                    sum((ytest==4) & (predictions_test==2)),
                    sum((ytest==4) & (predictions_test==3)),
                    sum((ytest==4) & (predictions_test==4)),
                    sum((ytest==4) & (predictions_test==5))],
                   
                   [sum((ytest==5) & (predictions_test==1)),
                    sum((ytest==5) & (predictions_test==2)),
                    sum((ytest==5) & (predictions_test==3)),
                    sum((ytest==5) & (predictions_test==4)),
                    sum((ytest==5) & (predictions_test==5))]]

print("Training confusion matrix:")
print(train_confusion[0])
print(train_confusion[1])
print(train_confusion[2])
print(train_confusion[3])
print(train_confusion[4])
print("Point guards: " + str(sum(ytrain == 1)))
print("Shooting guards: " + str(sum(ytrain == 2)))
print("Small Forwards: " + str(sum(ytrain == 3)))
print("Power Forwards: " + str(sum(ytrain == 4)))
print("Centers: " + str(sum(ytrain == 5)))
print("Score: " + str(sum(ytrain == predictions_train) / float(len(ytrain))))

print()
print("Testing confusion matrix:")
print(test_confusion[0])
print(test_confusion[1])
print(test_confusion[2])
print(test_confusion[3])
print(test_confusion[4])
print("Point guards: " + str(sum(ytest == 1)))
print("Shooting guards: " + str(sum(ytest == 2)))
print("Small Forwards: " + str(sum(ytest == 3)))
print("Power Forwards: " + str(sum(ytest == 4)))
print("Centers: " + str(sum(ytest == 5)))
print("Score: " + str(sum(ytest == predictions_test) / float(len(ytest))))

plt.plot(range(len(clf.training_loss)), clf.training_loss)
plt.show()
