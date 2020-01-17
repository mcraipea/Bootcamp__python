from book import Book
from recipe import Recipe

choix = -1
while choix != "0":
	print ("")
	print ("Que souhaitez vous faire?")
	print ("1 - Ajouter une recette")
	print ("2 - Voir toutes les recettes")
	print ("3 - Voir une recette en detail")
	choix = input("Quelle est votre choix : ")

	book = Book()

	if choix == "1":
		s = input("Quelle recette voulez vous ajouter?\n")
		book.add_recipe(s)

	elif choix == "2":
		book.print_all_recipe()

	elif choix == "3":
		imprim = input("Quelle recette voulez vous voir?\n")
		book.print_one_recipe(imprim)

