import numpy as np

class Classify:
    def __init__(self,k=6,d=4,lr=1e-3,max_epoch=40, verbose = True): # k is number of classes, d is number of features
        # k: number of classes, d: number of features
        # lr: learning rate,
        # max_epoch: maximum number of training epochs
        self.k = k
        self.d = d
        self.weight = np.zeros([k,d])
        self.bias = np.zeros(k)
        self.lr = lr
        self.max_epoch = max_epoch
        self.training_loss = []
        self.verbose = verbose

    def fit(self, Xtrain, ytrain):
        ##### implement stochastic gradient descent (with batch size fixed to 1)
        for epoch in range(self.max_epoch):
            if self.verbose: print("Epoch: " + str(epoch + 1))
            #### shuffle the training samples at the begining of each epoch using np.random.shuffle
            Xtrain, ytrain = self.shuffle(Xtrain, ytrain)
            
            training_loss = 0
            for i in range(len(Xtrain)):
                #### iterate through the training samples and update the weight matrix on a sample-basis one-by-one
                x = Xtrain[i]
                y = ytrain[i]

                for class_num in range(len(self.weight)):

                    phi = self.softmax(x, class_num)
                    self.weight[class_num] = self.weight[class_num] + self.lr * (y[class_num] - phi) * x
                    self.bias[class_num] = self.bias[class_num] + self.lr * (y[class_num] - phi)
                    
                    training_loss -= y[class_num] * np.log(phi)

            self.training_loss.append(training_loss)

            if self.verbose: print("Training loss: " + str(training_loss))
                
            # early stopping based on training loss
            if training_loss <= 1e-3:
                break

    def predict(self, Xtest):
        #### predic the confidences for different classes
        prediction = np.empty([len(Xtest),self.k])
        for i in np.arange(len(Xtest)):
            for class_num in range(self.k):
                prediction[i][class_num] = self.softmax(Xtest[i], class_num)
            
        return prediction

    def params(self):
        return self.weight, self.bias

    def shuffle(self, Xtrain, ytrain):
        shuffled_index = np.arange(0, len(Xtrain))
        np.random.shuffle(shuffled_index)

        ret_Xtrain = np.empty(Xtrain.shape)
        ret_ytrain = np.empty(ytrain.shape)
        for i in np.arange(0,len(Xtrain)):
            ret_Xtrain[i] = Xtrain[shuffled_index[i]]
            ret_ytrain[i] = ytrain[shuffled_index[i]]
        return ret_Xtrain, ret_ytrain

    def sigmoid(self, s):
        try:
            return float(1./(1+np.e**(-1*s)))
        except OverflowError:
            return 0.0

    def softmax(self, x, class_num):
        normalizing_term = 0
        offset = max(self.weight.dot(x))
        for i in range(self.k):
            normalizing_term += np.exp(self.weight[i].dot(x) + self.bias[i] - offset)
        numerator = np.exp(self.weight[class_num].dot(x) + self.bias[class_num] - offset)
        return numerator / normalizing_term
