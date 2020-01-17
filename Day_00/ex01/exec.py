import sys

def ft_case(str):
	dest = ""
	for c in str:
		if (c.isupper()) == True:
			dest+= c.lower()
		else:
			dest+= c.upper()
	return dest

def ft_reverse(str):
    dest = ""
    for char in str:
        dest = char + dest
    return dest

if (len(sys.argv) > 1):
	dest = ""
	dest2 = ""
	for i in range(len(sys.argv) - 1, 1, -1):
		dest = ft_case(sys.argv[i])
		dest2 = ft_reverse(dest)
		print(dest2, end=" ")
	dest = ft_case(sys.argv[1])
	dest2 = ft_reverse(dest)
	print (dest2)
else:
	sys.exit()
