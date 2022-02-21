# Introducing program and menu
print("Welcome to Pthon Pizza Deliveries!")
print("\nOur menu:\nSmall Pizza: $15\nMedium Pizza: $20\nLarge Pizza: $25\n\nPepperoni for Small Pizza: +$2")
print("Pepperoni for Medium or Large Pizza: $+3\n\nExtra Cheese: $+1")

# Asking for pizza characteristics they want

size = input("Size (S, M, L): ")
add_pepperoni = input("Pepperoni (y/n): ")
extra_cheese = input("Extra Cheese (y/n): ")
bill = 0

# Computing final pizza price 
if size == "S": 
    bill += 15
    if add_pepperoni: bill += 2
elif size == "M": 
    bill += 20
    if add_pepperoni: bill += 3
else: 
    bill += 25
    if add_pepperoni: bill += 3

if extra_cheese == "y":
    bill += 1
    
# Outputting price
print(f"Your pizza costs ${bill}")