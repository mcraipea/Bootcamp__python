import numpy as np
from collections.abc import Iterable

def sigmoid_(x):
	if isinstance(x, Iterable):
		a = []
		for item in x:
			a.append(1 / (1 + np.exp(-item)))
		return a
	else:
		return (1 / (1 + np.exp(-x)))

# x = -4
# print(sigmoid_(x))
# x= 2
# print(sigmoid_(x))
# x = [-4, 2, 0]
# print(sigmoid_(x))