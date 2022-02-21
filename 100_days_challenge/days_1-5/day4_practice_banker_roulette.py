# This is a banker roulette game, played often among wealthy financial individuals. 
# A group's bill is payed exclusively by one member randomly
 
import random

# Asking and saving input to an array via split method
names = input("Eneter every members' names, seperated by a space: ").split(" ")

# Generating a random number for array index
random_number = random.randint(0, len(names)-1)

# Printing a random members' name
print(f"{names[random_number]} has to pay")
