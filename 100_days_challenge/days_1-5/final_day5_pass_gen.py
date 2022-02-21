# This is a password generator

# Arrays to choose characters from 
import random 
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Introducing program and saving input. Initializing final password list and string
print("Welcome to the PyPassword Generator!")
amount_letters= int(input("How many letters would you like in your password?\n")) 
amount_symbols = int(input(f"How many symbols would you like?\n"))
amount_numbers = int(input(f"How many numbers would you like?\n"))
password_list = []
password_string = ""

# Looping through number of each character type and appending a random one to password list
for _ in range(amount_letters):
    password_list.append(random.choice(letters))

for _ in range(amount_numbers):
    password_list.append(random.choice(numbers))

for _ in range(amount_symbols):
    password_list.append(random.choice(symbols))
    
# Random shuffling password_list and converting into string with join method
random.shuffle(password_list)
print(password_string.join(password_list))