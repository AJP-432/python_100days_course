# Introducing program
print("Welcome to the tip calculator.")

# Collecting bill amount, tip percentage, and number of people
bill = float(input("What was the total bill: $"))
percentage = int(input("What percentage tip would you like to give (10, 12, & 15 are typical): "))/100
people = int(input("How many people are splitting the bill: "))

# Calculating how much everyone has to pay
owe = round(((bill + bill * percentage)/people), 2)

# Outputting amount everyone should pay 
print(f"Each person should give ${owe}")  