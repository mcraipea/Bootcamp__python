import numpy as np

class NumPyCreator:
	def __init__(self):
		pass
	def from_list(self, lst):
		return (np.array(lst))
	def from_tuple(self, tpl):
		return (np.array(tpl))
	def from_iterable(self, itr):
		return (np.array(itr))
	def from_shape(self, shape, value=0):
		return (np.full(shape, value))
	def random(self, shape):
		return (np.random.rand(shape[0],shape[1]))
	def identity(self, n):
		return (np.eye(n))

print (np.pi)
npc = NumPyCreator()
print (npc.from_list([[1,2,3],[6,3,4]]))
print (npc.from_tuple(("a", "b", "c")))
print (npc.from_iterable(range(5)))
shape=(3,5)
print (npc.from_shape(shape, 2))
shap=(4,7)
print (npc.random(shap))
print (npc.identity(4))
