import pandas as pd

class FileLoader():
	def __init__(self):
		pass

	def load(self, path, sep=','):
		df = pd.read_table(path, sep)
		#print ('Loading dataset of dimensions '+str(df.shape))
		return (df)

	def display(self, df, n):
		if n > 0:
			print(df.head(n))
		else:
			print(df.tail(abs(n)))


#fl = FileLoader()
#df = fl.load("./athlete_events.csv")
#fl.display(df, 13)