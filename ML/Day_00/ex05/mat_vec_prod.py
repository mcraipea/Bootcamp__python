import numpy as np
from dot import dot

def mat_vec_prod(x, y):
	"""Computes the product of two non-empty numpy.ndarray, using a
	for-loop. The two arrays must have compatible dimensions.
	Args:
	x: has to be an numpy.ndarray, a matrix of dimension m * n.
	y: has to be an numpy.ndarray, a vector of dimension n * 1.
	Returns:
	The product of the matrix and the vector as a vector of dimension m *
	1.
	None if x or y are empty numpy.ndarray.
	None if x and y does not share compatibles dimensions.
	Raises:
	This function should not raise any Exception.
	"""
	
	m = len(x)
	n = len(y)
	if m == 0 or n == 0:
		return None
	prod = []
	somme = 0
	try:
		for i in range (0,m):
			prod2 = []
			prod2.append(int(dot(x[i],y)))
			prod.append(prod2)
	except IndexError:
		return None
	return np.array(prod)


# W = np.array([
#     [ -8, 8, -6, 14, 14, -9, -4],
#     [ 2, -11, -2, -11, 14, -2, 14],
#     [-13, -2, -5, 3, -8, -4, 13],
#     [ 2, 13, -14, -15, -14, -15, 13],
#     [ 2, -1, 12, 3, -7, -3, -6]])
# X = np.array([0, 15, -9, 7, 12, 3, -21]).reshape((7,1))
# Y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape((7,1))
# print(mat_vec_prod(W, X))
# print(W.dot(X))
# print(mat_vec_prod(W, Y))
# print(W.dot(Y))
