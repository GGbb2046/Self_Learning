import numpy as np
import pandas as pd
#%matplotlib inline
import matplotlib.pyplot as plt

df = pd.read_csv('LR.csv', header = None)
df.head()

theta = [0,0]   

def hypothesis(theta, X):
    return theta[0] + theta[1]*X
def cost_calc(theta, X, y):
    return (1/2*m) * np.sum((hypothesis(theta, X) - y)**2)


m = len(df)
def gradient_descent(theta, X, y, epoch, alpha):
    cost = []
    i = 0
    while i < epoch:
        hx = hypothesis(theta, X)
        theta[0] -= alpha*(sum(hx-y)/m)
        theta[1] -= (alpha * np.sum((hx - y) * X))/m
        cost.append(cost_calc(theta, X, y))
        i += 1
    return theta, cost

def predict(theta, X, y, epoch, alpha):
    theta, cost = gradient_descent(theta, X, y, epoch, alpha)
    return hypothesis(theta, X), cost, theta


y_predict, cost, theta = predict(theta, df[0], df[1], 2000, 0.01)

plt.figure()
plt.scatter(df[0], df[1], label = 'Original y')
plt.scatter(df[0], y_predict, label = 'predicted y')
plt.legend(loc = "upper left")
plt.xlabel("input feature")
plt.ylabel("Original and Predicted Output")
plt.show()

plt.figure()
plt.scatter(range(0, len(cost)), cost)
plt.show()