class CsvReader():
	
	def __enter__(self):
		try:
			self.file = open(self.name, 'r')
		#	return (1)
		except IOError:
			print ('Error : File not found')
			return (None)
		if self.file.mode == 'r':
			self.content = self.file.readlines()
		#self.content.replace(" ", "")
		for string in self.content:
			self.string = string.split(self.sep)
		#for line in self.content:
		#	print (line)
		return (self.string)

	def __init__(self, name=None, sep=',', header=False, skip_top=0, skip_bottom=0):
		self.file = None
		self.name = name
		self.sep = sep

	def __exit__(self, type, value, traceback):
		if self.file != None:
			self.file.close()

	def truc(self):
		print ('truc')

with CsvReader("good.csv") as content:
	for line in content:
		print (line)
