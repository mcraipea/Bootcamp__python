import re

def generator(text, sep=" ", option=None):
	
	separator = ""
	for c in sep:
		separator = separator + c + '|'
	lst = re.split(separator, text)
	
	if option == "ordered":
		lst = sorted(lst)
	
	for ele in lst:
		if ele == "":
			lst.remove(ele)
	for ele in lst:
		if ele == "":
			lst.remove(ele)
	if option == "unique":
		lst = set(lst)
	for s in lst:
		yield (s)



for i in generator("Bonjour, bien-,venu b b a a tous", ', -', "unique"):
	print(i)