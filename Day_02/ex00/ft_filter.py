def ft_filter(fct, lst):
	result = []
	for i in lst:
		if fct(i) == True:
			result.append(i)
	return result

def fun(variable): 
    letters = ['a', 'e', 'i', 'o', 'u'] 
    if (variable in letters): 
        return True
    else: 
        return False

lst = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r'] 
filtered_lst = ft_filter(fun, lst)
print (filtered_lst)
