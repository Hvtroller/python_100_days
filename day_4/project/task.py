# include random module
import random
import my_module

random_integer = random.randint(1, 10) # generate random number between 1 and 10

# compare random_integer with my_module.pi
print(random_integer)
print("is my number bigger than pi? " + str(random_integer > my_module.pi))

# create a random float number and compare it with pi
random_float = random.uniform(1, 10)
print(random_float)
print("is my number bigger than pi? " + str(random_float > my_module.pi))
