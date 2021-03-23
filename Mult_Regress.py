import pandas as pd
import numpy as np
df = pd.read_csv('ex1data2.txt', header = None)
df.head()

df = pd.concat([pd.Series(1, index=df.index, name='00'), df], axis=1)
df.head()

X = df.drop(columns=2)
y = df.iloc[:, 3]

for i in range(1, len(X.columns)):
    X[i-1] = X[i-1]/np.max(X[i-1])
X.head()

theta = np.array([0]*len(X.columns))
#Output: array([0, 0, 0])

m = len(df)
def hypothesis(theta, X):
    return theta*X

def computeCost(X, y, theta):
    y1 = hypothesis(theta, X)
    y1=np.sum(y1, axis=1)
    return sum(np.sqrt((y1-y)**2))/(2*47)


def gradientDescent(X, y, theta, alpha, i):
    J = []  #cost function in each iterations
    k = 0
    while k < i:        
        y1 = hypothesis(theta, X)
        y1 = np.sum(y1, axis=1)
        for c in range(0, len(X.columns)):
            theta[c] = theta[c] - alpha*(sum((y1-y)*X.iloc[:,c])/len(X))
        j = computeCost(X, y, theta)
        J.append(j)
        k += 1
    return J, j, theta

J, j, theta = gradientDescent(X, y, theta, 0.05, 10000)
y_hat = hypothesis(theta, X)
y_hat = np.sum(y_hat, axis=1)

#%matplotlib inline
import matplotlib.pyplot as plt
plt.figure()
plt.scatter(x=list(range(0, 47)),y= y, color='blue')         
plt.scatter(x=list(range(0, 47)), y=y_hat, color='black')
plt.show()

plt.figure()
plt.scatter(x=list(range(0, 10000)), y=J)
plt.show()