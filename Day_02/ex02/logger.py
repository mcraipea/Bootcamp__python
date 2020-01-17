import time
import datetime
from random import randint
import logging

class CoffeeMachine():
	
	water_level = 100

	def log(func):
		logging.basicConfig(filename='machine.log', format='(mcraipea)Running: %(message)s', level=logging.INFO)
		def wrapper(*args, **kwargs):
			start = time.time()
			response = func(*args, **kwargs)
			end = time.time()
			exec_time = end - start
			datetime.timedelta(seconds=exec_time)
			if exec_time > float(0.0009)
				exec_time = round(exec_time, 3)
			s = str(func.__name__).replace("_", " ").title()+"   [ exec-time = "+str(exec_time)+" ]"
			logging.info(s)
			return response
		return wrapper


	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
			return False
	
	@log
	def boil_water(self):
		return "boiling..."
    
	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")
    
	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")

if __name__ == "__main__":
	
	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()
	
	machine.make_coffee()
	machine.add_water(70)