import numpy as np

def mat_mat_prod(x, y):
	"""Computes the product of two non-empty numpy.ndarray, using a
	for-loop. The two arrays must have compatible dimensions.
	Args:
	x: has to be an numpy.ndarray, a matrix of dimension m * n.
	y: has to be an numpy.ndarray, a vector of dimension n * p.
	Returns:
	The product of the matrices as a matrix of dimension m * p.
	None if x or y are empty numpy.ndarray.
	None if x and y does not share compatibles dimensions.
	Raises:
	This function should not raise any Exception.
	"""
	m = x.shape[0]
	n = x.shape[1]
	p = y.shape[1]
	array = []

	for j in range(0,p):
		for i in range(0,m):
			somme = 0
			for k in range (0,n):
				somme += x[j][k] * y[k][i]
			array.append(somme)
	return (np.array(array).reshape(m,p))





# W = np.array([
#     [ -8, 8, -6, 14, 14, -9, -4],
#     [ 2, -11, -2, -11, 14, -2, 14],
#     [-13, -2, -5, 3, -8, -4, 13],
#     [ 2, 13, -14, -15, -14, -15, 13],
#     [ 2, -1, 12, 3, -7, -3, -6]])
# Z = np.array([
#     [ -6, -1, -8, 7, -8],
#         [ 7, 4, 0, -10, -10],
#         [ 7, -13, 2, 2, -11],
#         [ 3, 14, 7, 7, -4],
#         [ -1, -3, -8, -4, -14],
#         [ 9, -14, 9, 12, -7],
#         [ -9, -4, -10, -3, 6]])
# print(mat_mat_prod(W, Z))
# print(W.dot(Z))
# print(mat_mat_prod(Z,W))
# print(Z.dot(W))