import numpy as np
from sigmoid import sigmoid_

def log_gradient_(x, y_true, y_pred):
	# gradient = []
	# m = len(x)
	# for i in range(m):
	# 	gradient.append(np.dot(y_pred - y_true, x))
	# return gradient
	return (np.dot(y_pred - y_true, x))





# Test n.1
x = [1, 4.2] # 1 represent the intercept
y_true = 1
theta = [0.5, -0.5]
x_dot_theta = sum([a*b for a, b in zip(x, theta)])
y_pred = sigmoid_(x_dot_theta)
print(log_gradient_(x, y_pred, y_true))
# [0.8320183851339245, 3.494477217562483]

# Test n.2
x = [1, -0.5, 2.3, -1.5, 3.2]
y_true = 0
theta = [0.5, -0.5, 1.2, -1.2, 2.3]
x_dot_theta = sum([a*b for a, b in zip(x, theta)])
y_pred = sigmoid_(x_dot_theta)
print(log_gradient_(x, y_true, y_pred))
# [0.99999685596372, -0.49999842798186, 2.299992768716556, -1.4999952839455801, 3.1999899390839044]
