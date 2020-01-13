import sys

if (len(sys.argv) == 1):
	sys.exit()
elif (len(sys.argv) > 2):
	print ("ERROR")
else:
	str = sys.argv[1].lstrip('-+')
	if str.isdigit() == False:
		 print ("ERROR")
	else:
		i = int(str)
		if i == 0:
			print ("I'm Zero.")
		elif (i % 2) == 0:
			print ("I'm Even.")
		else:
			print ("I'm Odd.")


