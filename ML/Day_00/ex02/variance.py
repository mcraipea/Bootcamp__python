import numpy as np

def variance(x):
	"""Computes the variance of a non-empty numpy.ndarray, using a for-loop.
	Args:
	x: has to be an numpy.ndarray, a vector.
	Returns:
	The variance as a float.
	None if x is an empty numpy.ndarray.
	Raises:
	This function should not raise any Exception.
	"""
	if len(x) == 0:
		return None
	moy = 0.0
	var = 0.0
	for i in range(0, len(x)):
		moy += float(x[i])
	moy /= len(x)
	for i in range(0, len(x)):
		var += float((x[i] - moy) * (x[i] - moy))
	var /= len(x)
	return (var)


#X = np.array([0, 15, -9, 7, 12, 3, -21])
#print(variance(X))
#print(np.var(X))
#X = np.array([0, 15, -9, 7, 12, 3, -21])
#print(variance(X/2))
#print(np.var(X/2))