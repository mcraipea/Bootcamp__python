import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

class ImageProcessor:
	def __init__(self):
		pass

	def load(self, path):
		try:
			self.png = open(path, 'r')
		except IOError:
			print ('Error : File not found')
			return (None)
		image = mpimg.imread(path)
		print (image.shape[0:2])
		return (image)

	def display(self, array):
		imgplot = plt.imshow(array)
		plt.show()




imp = ImageProcessor()
arr = imp.load("./42AI.png")
print (arr)
imp.display(arr)
