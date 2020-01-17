import numpy as np
from ImageProcessor import ImageProcessor
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

class ColorFilter:
	def __init__(self):
		pass

	def invert(self, array):
		return (1 - array)
		
	def to_blue(self, array):
		self.imgbleu = np.zeros(array.shape)
		self.imgbleu [ : , : , 2] = array [ : , : , 2]
		return (self.imgbleu)

	def to_green(self, array):
		self.imggreen = array
		self.imggreen [ : , : , 0] *= 0
		self.imggreen [ : , : , 2] *= 0
		self.imggreen [ : , : , 1] = array [ : , : , 1]
		return (self.imggreen)

	def to_red(self, array):
		imgred = array
		imgred = self.to_blue(array) - self.to_blue(array)
		imgred [ : , : , 0] = array [ : , : , 0]
		return (imgred)

	def celluloid(self, array, threshold=25):
		return (np.linspace(array, 0, 50)[threshold])

	def to_grey(self, array):
		return (np.dot(array[...,:3], [0.299, 0.587, 0.144]))

	def to_nb(self, array, threshold=25):
		pass



imp = ImageProcessor()
arr = imp.load("./42AI.png")
cf = ColorFilter()
#imp.display(arr)
#imp.display(cf.invert(arr))
#imp.display(cf.to_red(arr))
#imp.display(cf.to_blue(arr))
#imp.display(cf.to_green(arr))
#imp.display(cf.celluloid(arr, 35))
#imp.display_grey(cf.to_grey(arr))
