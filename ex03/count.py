def text_analyzer(str = ""):
	"""This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""
	if len(str) == 0:
		str = input("Please enter your text : ")
	upper = 0
	lower = 0
	digit = 0
	punct = 0
	space = 0
	
	print ("The text contains", len(str), "characters:")
	for c in str:
		if c.isupper() == True:
			upper+= 1
		elif c.islower() == True:
			lower+= 1
		elif c.isdigit() == True:
			digit+= 1
		elif c.isspace() == True:
			space+= 1
		else:
			punct+= 1
	print ("- ", upper, "upper letters")
	print ("- ", lower, "lower letters")
	print ("- ", digit, "digits")
	print ("- ", punct, "punctuation marks")
	print ("- ", space, "spaces")
