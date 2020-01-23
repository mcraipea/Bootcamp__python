import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import mean_squared_error

from FileLoader import FileLoader
from mylinearregression import MyLinearRegression as MyLR

m = 20
theta1_true = 0.5
x = np.linspace(-1,1,m)
y = theta1_true * x

def cost_func(theta1):
    """The cost function, J(theta1) describing the goodness of fit."""
    theta1 = np.atleast_2d(np.asarray(theta1))
    return np.average((y-hypothesis(x, theta1))**2, axis=1)/2
def hypothesis(x, theta1):
    """Our "hypothesis function", a straight line through the origin."""
    return theta1*x

data = pd.read_csv("./are_blue_pills_magics.csv")
Xpill = np.array(data["Micrograms"]).reshape(-1,1)
Yscore = np.array(data["Score"]).reshape(-1,1)
# Yscore = np.reshape(1,1)
# print(Yscore)
linear_model1 = MyLR(np.array([[89.0], [-8]]))
linear_model2 = MyLR(np.array([[89.0], [-6]]))
Y_model1 = linear_model1.predict_(Xpill)
Y_model2 = linear_model2.predict_(Xpill)

mse = mean_squared_error(Yscore, Y_model1)

linear_model1.fit_(Xpill, Yscore, alpha = 0.01, n_cycle=2000)
# print(linear_model1.theta)

fig = plt.figure()
ax = plt.axes()
# plt.scatter(Xpill, Yscore, color='blue', label='Pillule')
# plt.scatter(Xpill, Y_model1, color="g")
# plt.plot(Xpill, Y_model1, color="g")
# plt.show()
abscisse = np.linspace(-14.4,-3.8)
ordonnee = linear_model1.cost_(abscisse[:,np.newaxis], Yscore)

plt.plot(abscisse, ordonnee, color="g")
plt.tight_layout()
plt.show()

