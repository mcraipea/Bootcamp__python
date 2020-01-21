import numpy as np
from pred import predict_ 

def cost_(theta, X, Y):
	"""
	Description:
	Calculates all the elements 0.5*M*(y_pred - y)^2 of the cost
	function.
	Args:
	theta: has to be a numpy.ndarray, a vector of dimension (number of
	features + 1, 1).
	X: has to be a numpy.ndarray, a matrix of dimension (number of
	training examples, number of features).
	Returns:
	J_elem: numpy.ndarray, a vector of dimension (number of the training
	examples,1).
	None if there is a dimension matching problem between X, Y or theta.
	Raises:
	This function should not raise any Exception.
	"""
	predictions = predict_(theta,X)
	squared_errors = np.square(predictions - Y)
	return (np.sum(squared_errors) / (2 * len(Y)))

# X1 = np.array([[0.], [1.], [2.], [3.], [4.]])
# theta1 = np.array([[2.], [4.]])
# Y1 = np.array([[2.], [7.], [12.], [17.], [22.]])
# print(cost_(theta1, X1, Y1))
# X2 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
# theta2 = np.array([[0.05], [1.], [1.], [1.]])
# Y2 = np.array([[19.], [42.], [67.], [93.]])
# print(cost_(theta2, X2, Y2))