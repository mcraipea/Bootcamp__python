import numpy as np
from cost_function import cost_
from pred import predict_

def fit_(theta, X, Y , alpha=0.05, n_cycle=1000):
	m = X.shape[0]
	X = np.append(np.ones((m,1)),X,axis=1)
	for n in range(n_cycle):
		predictions = np.dot(X, theta)
		errors = predictions - Y
		gradient = np.dot(X.transpose(), errors)
		theta -= alpha * gradient / len(Y)
	return theta


# X1 = np.array([[0.], [1.], [2.], [3.], [4.]])
# Y1 = np.array([[2.], [6.], [10.], [14.], [18.]])
# theta1 = np.array([[1.], [1.]])
# theta1 = fit_(theta1, X1, Y1, alpha = 0.01, n_cycle=2000)
# print(theta1)
# X2 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
# Y2 = np.array([[19.6], [-2.8], [-25.2], [-47.6]])
# theta2 = np.array([[42.], [1.], [1.], [1.]])
# theta2 = fit_(theta2, X2, Y2, alpha = 0.0005, n_cycle=42000)
# print(theta2)
# print(predict_(theta2, X2))