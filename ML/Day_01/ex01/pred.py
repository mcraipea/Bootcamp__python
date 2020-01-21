import numpy as np

def predict_(theta, X):
	"""
	Description:
	Prediction of output using the hypothesis function (linear model).
	Args:
	theta: has to be a numpy.ndarray, a vector of dimension (number of
	features + 1, 1).
	X: has to be a numpy.ndarray, a matrix of dimension (number of
	training examples, number of features).
	Returns:
	pred: numpy.ndarray, a vector of dimension (number of the training
	examples,1).
	None if X does not match the dimension of theta.
	Raises:
	This function should not raise any Exception.
	"""
	m = X.shape[0]
	X= np.append(np.ones((m,1)),X,axis=1)
	return (np.dot(X, theta))
