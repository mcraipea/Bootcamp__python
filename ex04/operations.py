import sys

def ft_error():
	print ("Usage: python operations.py")
	print ("Example:")
	print ("    python operations.py 10 3")
	sys.exit()

if (len(sys.argv) < 3) or (len(sys.argv) > 3):
	if (len(sys.argv) > 3):
		print ("InputError: too many arguments")
		print ()
	ft_error()
else:
	try:
		n1 = int(sys.argv[1])
	except (TypeError, ValueError, AttributeError):
		 print ("InputError: only numbers")
		 ft_error()
	try:
		n2 = int(sys.argv[2])
	except (TypeError, ValueError, AttributeError):
		 print ("InputError: only numbers")
		 ft_error()
	print ("Sum:         ", n1 + n2)
	print ("Difference:  ", n1 - n2)
	print ("Product:     ", n1 * n2)
	if n2 == 0:
		print ("Quotient:    ERROR (div by zero)")
		print ("Remainder:   ERROR (div by zero)")
	else:
		print ("Quotient:    ", n1 / n2)
		print ("Remainder:   ", n1 % n2)
