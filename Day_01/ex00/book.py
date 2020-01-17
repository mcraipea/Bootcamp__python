from recipe import Recipe

class Book:
	"""
	Bouquin qui receuille toutes les recettes
	"""
	
	nb_recette = 0  #attribut de classe
	lst = []
	def __init__(self):
		pass

	def add_recipe(self, nom):
		Book.lst.append(nom)
		nom = Recipe()
		elem = input("Merci de renseigner : Niveau de 1 - 5\Tps de prepa\Type de repas?\n")
		elem = elem.split()
		nom.name = nom
		nom.add_elem(elem[0], elem[1], elem[2])
		Book.nb_recette += 1

	def print_all_recipe(self):
		for recipe in Book.lst:
			print (recipe)

	def print_one_recipe(self, choix):
		for recipe in Book.lst:
			if choix == recipe:
				#recipe = Recipe()
				recipe.print_recipe()