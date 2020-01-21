import numpy as np
from math import sqrt

def std(x):
	"""Computes the standard deviation of a non-empty numpy.ndarray, using a
	for-loop.
	Args:
	x: has to be an numpy.ndarray, a vector.
	Returns:
	The standard deviation as a float.
	None if x is an empty numpy.ndarray.
	Raises:
	This function should not raise any Exception.
	"""
	if len(x) == 0:
		return None
	moy = 0.0
	var = 0.0
	ecart = 0.0
	for i in range(0, len(x)):
		moy += float(x[i])
	moy /= len(x)
	for i in range(0, len(x)):
		var += float((x[i] - moy) * (x[i] - moy))
	var /= len(x)
	ecart = sqrt(var)
	return (ecart)


#X = np.array([0, 15, -9, 7, 12, 3, -21])
#print(std(X))
#print(np.std(X))
#Y = np.array([2, 14, -13, 5, 12, 4, -19])
#print(std(Y))
#print(np.std(Y))