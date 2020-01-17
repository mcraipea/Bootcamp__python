class Evaluator:

	sum = 0

	def zip_evaluate(self, words = [], coefs = []):
		if len(words) != len(coefs):
			return (-1)
		else:
			for ele,co in zip(words,coefs):
				Evaluator.sum += len(co) * ele
		print (Evaluator.sum) 
			