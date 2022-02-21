# This is a heads or tails simulator

# Importing random module
import random
# Introducing program
print("This is a heads or tails simulator")
# Generating 0 or 1 which are heads and tails, respecitvely
chance = random.randint(0,1)
# Printing result 
if chance == 0: 
    print("It's heads!")
else: 
    print("It's tails!")
    
