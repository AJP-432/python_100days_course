# Asking for height and weight input
height = float(input("What is your height in meters: "))
weight = float(input("What is your weight in kilograms: "))

# Calculating BMI (formula is weight/height^2)
bmi = str(round(weight/(height ** 2), 2))

# Printing BMI
print("Your BMI is " + bmi)

