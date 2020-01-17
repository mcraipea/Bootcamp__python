from FileLoader import FileLoader

def youngestFellah(df, year):
	df1 = df.loc[(df['Sex']=="M") & (df['Year']==year)]
	df1 = df1.sort_values(by='Age').head(1)
	i = df1.iloc[0,3]
	df2 = df.loc[(df['Sex']=="F") & (df['Year']==year)]
	df2 = df2.sort_values(by='Age').head(1)
	i2 = df2.iloc[0,3]
	print ("{'f': "+str(i2)+", 'm': "+str(i)+"}")


fl = FileLoader()
data = fl.load('./athlete_events.csv')
youngestFellah(data,2008)
