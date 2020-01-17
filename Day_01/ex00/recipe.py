class Recipe:
	def __init__(self):
		self.name = ""
		self.cooking_lvl = 0
		self.cooking_time = 0
		self.ingredients = ""
		self.description = ""
		self.recipe_type = ""

	def add_elem(self, lvl, tps, meal):
		self.cooking_lvl = lvl
		self.cooking_time = tps
		self.recipe_type = meal

	def print_recipe(self):
		print("Nom de la recette : "+self.name)
		print("Difficulte : {}".format(self.cooking_lvl))
		print("Temps de preparation : {}".format(self.cooking_time))
		print("Ingredients : "+self.ingredients)
		print("Description : "+self.description)
		print("A quel moment : "+self.recipe_type)
	