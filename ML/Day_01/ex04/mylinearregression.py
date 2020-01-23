import numpy as np


class MyLinearRegression():
	def __init__(self, theta):
		self.theta = theta
		pass

	def fit_(self, X, Y, alpha=0.05, n_cycle=1000):
		self.m = X.shape[0]
		self.X = np.append(np.ones((self.m,1)),X,axis=1)
		for n in range(n_cycle):
			self.predictions = np.dot(self.X, self.theta)
			self.errors = self.predictions - Y
			self.gradient = np.dot(self.X.transpose(), self.errors)
			self.theta -= alpha * self.gradient / len(Y)
		return self.theta

	def predict_(self, X):
		self.m = X.shape[0]
		self.X = np.append(np.ones((self.m,1)),X,axis=1)
		return (self.X @ self.theta)

	def cost_(self, X, Y):
		self.predictions = self.predict_(X)
		self.squared_errors = np.square(self.predictions - Y)
		return (np.sum(self.squared_errors) / (2 * len(Y)))

	# def mse_(self, y, y_hat):
	# 	somme = 0.0
	# 	for i in range(0,len(y)):
	# 		somme += (y[i] - y_hat[i]) ** 2
	# 	somme /= len(y)
	# 	return (somme)




# X1 = np.array([[0.], [1.], [2.], [3.], [4.]])
# Y1 = np.array([[2.], [6.], [10.], [14.], [18.]])
# theta1 = MyLinearRegression([[1.], [1.]])
# theta1.fit_(X1, Y1, alpha = 0.01, n_cycle=2000)
# print(theta1.theta)