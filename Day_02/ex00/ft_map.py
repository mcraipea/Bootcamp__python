def ft_map(fct, lst):
	result = []
	for i in lst:
		result.append(fct(i))
	return result

def add(n):
	return (n + n)

numbers = [1, 2, 3, 4]
print (numbers)
result = ft_map(add, numbers)
print(result)
