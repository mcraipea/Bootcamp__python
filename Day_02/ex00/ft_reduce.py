def ft_reduce(fct, lst):
	result = lst[0]
	for i in range(1, len(lst)):
		result = fct(result, lst[i])
	return result

def do_sum(x1, x2):
	return (x1 + x2)

def do_mul(x1, x2):
	return (x1 * x2)

print(ft_reduce(do_sum, [1, 2, 3, 4]))
print(ft_reduce(do_mul,[1, 2, 3, 4]))
