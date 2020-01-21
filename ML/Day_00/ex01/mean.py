import numpy as np

def mean(x):
	"""Computes the mean of a non-empty numpy.ndarray, using a for-loop.
	Args:
	x: has to be an numpy.ndarray, a vector.
	Returns:
	The mean as a float.
	None if x is an empty numpy.ndarray.
	Raises:
	This function should not raise any Exception.
	"""
	if len(x) == 0:
		return None
	moy = 0.0
	for i in range(0, len(x)):
		moy += float(x[i])
	moy /= len(x)
	return moy


#X = np.array([0, 15, -9, 7, 12, 3, -21])
#print(mean(X))
#X = np.array([0, 15, -9, 7, 12, 3, -21])
#print(mean(X ** 2))