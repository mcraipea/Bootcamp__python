class Vector:
	def __init__(self, values):
		if isinstance(values, list) == True:
			self.values = values
			self.size = len(self.values)
		elif isinstance(values, int) == True:
			self.size = values
			self.values = []
			for i in range(0, values):
				self.values.append(float(i))
		elif isinstance(values, tuple) == True:
			self.size = values[1] - values[0]
			self.values = []
			for i in range(values[0],values[1]):
				self.values.append(float(i))

	def __mul__(self, r):
		new_list = []
		for f in self.values:
			new_list.append(f * r)
		new = Vector(new_list)
		return new

	def __add__(self, r):
		new_list = []
		for f in self.values:
			new_list.append(f + r)
		new = Vector(new_list)
		return new
