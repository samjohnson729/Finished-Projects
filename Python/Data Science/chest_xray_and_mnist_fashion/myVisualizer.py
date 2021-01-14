from matplotlib import pyplot as plt
import numpy as np

def visualizer(data, model, title, labels):
    X = data[2]
    y = data[3]
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, .01))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

    plt.contourf(xx, yy, Z, alpha=0.4)
    plt.plot(X[y == 0, 0], X[y == 0, 1], 'r.')
    plt.plot(X[y == 1, 0], X[y == 1, 1], 'b*')
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.title(title)
    plt.legend(labels)
    return plt
