import sys
import string

n = int(sys.argv[2])
str = sys.argv[1]
for c in str:
	if c in string.punctuation:
		str = str.replace(c,'')
str = str.split()
for i in range(len(str) - 1, -1, -1):
	if len(str[i]) <= n:
		del str[i]
print(str)
