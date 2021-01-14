from preprocess import *
import numpy as np
from classifier import *
import matplotlib.pyplot as plt

data = preprocess("nba_games_raw.csv","team_stats.csv")
np.random.shuffle(data)

## PCA Analysis
y = data[:,-1]
X = data[:,:-1]
X = X - np.mean(X,0)
U, s, VT = np.linalg.svd(X, full_matrices = False)

s = s ** 2
dim_pca = 0
for i in range(2, len(s) + 1):
    var_percent = sum(s[:i])/sum(s)
    if var_percent > .99:
        print("Number of PCA components required = " + str(i))
        print("Percent of total variance in the first " + str(i) + " PCA components = " + str(var_percent))
        print("S = " + str(s))
        dim_pca = i
        break

X = X.dot(np.transpose(VT))
X = X[:,:dim_pca]

plt.figure()
plt.plot(X[y==0, 0], X[y==0, 1], 'go', label = "Away Win", alpha = .6)
plt.plot(X[y==1, 0], X[y==1, 1], 'rs', label = "Home Win", alpha = .6)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA of NBA Games")
plt.legend()
#plt.show()
plt.savefig("Plots/PCA_2")
plt.close()

## Set up the training/testing data for logistic regression
train_fraction = .65

Xtrain = data[:round(len(data) * train_fraction),:-1]
#Xtrain = X[:round(len(data) * train_fraction),:]
ytrain = data[:round(len(data) * train_fraction),-1]
Xtest = data[round(len(data) * train_fraction):,:-1]
#Xtest = X[round(len(data) * train_fraction):,:]
ytest = data[round(len(data) * train_fraction):,-1]

## One-Hot encoding for y-values
temp_train, temp_test = np.empty([len(ytrain),2]), np.empty([len(ytest),2])
for i in range(len(ytrain)):
    if ytrain[i] == 0: temp_train[i] = [0,1]
    if ytrain[i] == 1: temp_train[i] = [1,0]
for i in range(len(ytest)):
    if ytest[i] == 0: temp_test[i] = [0,1]
    if ytest[i] == 1: temp_test[i] = [1,0]
#ytrain = temp_train
#ytest = temp_test
    
clf = Classify(k=2,d=Xtrain.shape[1], lr = .0001, max_epoch = 60, verbose = False)

clf.fit(Xtrain,temp_train)
print(Xtrain[0])
predictions_train = clf.predict(Xtrain)
predictions_test = clf.predict(Xtest)

##### convert the predicted confidence to class labels
temp = np.empty(len(predictions_train))
for i in range(len(predictions_train)):
    temp[i] = np.argmin(predictions_train[i])
predictions_train = temp

temp = np.empty(len(predictions_test))
for i in range(len(predictions_test)):
    temp[i] = np.argmin(predictions_test[i])
predictions_test = temp

#plt.plot(clf.training_loss)
#plt.show()

# Construct the confusion matrix with the counts of correct and incorrect predictions.
confusion_matrix_train=np.array([[sum((ytrain==0) & (predictions_train==0)),sum((ytrain==1) & (predictions_train==0))],
                                 [sum((ytrain==0) & (predictions_train==1)),sum((ytrain==1) & (predictions_train==1))]])

confusion_matrix_test=np.array([[sum((ytest==0) & (predictions_test==0)),sum((ytest==1) & (predictions_test==0))],
                                [sum((ytest==0) & (predictions_test==1)),sum((ytest==1) & (predictions_test==1))]])
print(confusion_matrix_train)
print(confusion_matrix_test)
print("Train score = " + str((sum((ytrain==0) & (predictions_train==0))+sum((ytrain==1) & (predictions_train==1)))/float(len(ytrain))))
print("Test score = " + str((sum((ytest==0) & (predictions_test==0))+sum((ytest==1) & (predictions_test==1)))/float(len(ytest))))
