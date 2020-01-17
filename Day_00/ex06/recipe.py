import sys

cookbook = {'sandwich': {'meal': 'lunch', 'prep_time': '10 minutes', 'ingredients': ("ham", "bread", "cheese", "tomatoes")},
			'cake': {'meal': 'dessert', 'prep_time': '60 minutes', 'ingredients': ("flour", "sugar", "eggs")},
			'salad': {'meal': 'lunch', 'prep_time': '15 minutes', 'ingredients': ("avocado", "arugula", "spinach", "tomatoes")}}

def sandwich():
	print("To cook a sandwich for your "+cookbook['sandwich']['meal'])
	print("Take some")
	i = len(cookbook['sandwich']['ingredients']) - 1
	while (i >= 0):
		print("- "+cookbook['sandwich']['ingredients'][i])
		i-= 1
	print("And you need : "+cookbook['sandwich']['prep_time'])

print ("Faites votre choix")
print ("1 - Sandwich")
print ("2 - Cake")
print ("3 - Salad")
str = input("Merci de donner un chiffre : ")
if (str == '1'):
	sandwich()
	print ("Voulez vous enlever un ingredient?")
	str = input("Merci de donner un ingredient : ")
	if (str == cookbook['sandwich']['ingredients'][0]):
		del cookbook['sandwich']['ingredients'][0]
	i = len(cookbook['sandwich']['ingredients']) - 1
	while (i >= 0):
		print("- "+cookbook['sandwich']['ingredients'][i])
		i-= 1


