import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

class ScrapBooker:
	def __init__(self):
		pass

	def crop(self, array, dimensions, position=(0,0)): 
		print ('New resolution after crop is = ('+str(dimensions[0])+", "+str(dimensions[1])+')')
		return (array[position[0]:dimensions[0], position[1]:dimensions[1]])

	def thin(self, array, n, axis=0):
		return (np.delete(array, slice(0,array.shape[axis],n), axis))

	def juxtapose(self, array, n, axis=0):
		image = array
		for i in range(1,n):
			image = (np.concatenate((image, array), axis))
		return (image)

	def mosaic(self, array, dimensions):
		image = array
		for i in range(1,dimensions[0]):
			image = (np.concatenate((image, array), 0))
		image2 = image
		for i in range(1,dimensions[1]):
			image2 = (np.concatenate((image2, image), 1))
		return (image2)

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









imp = ScrapBooker()
arr = imp.load("./42AI.png")
imp.display(imp.crop(arr, (50, 50)))