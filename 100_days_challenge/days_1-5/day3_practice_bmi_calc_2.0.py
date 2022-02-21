# Asking for height and weight input
weight = float(input("Weight in kilograms: "))
height = float(input("Height in meters: "))

# Calculating BMI (formula is weight/height^2)
bmi = round(weight/height ** 2)

# Determining which BMI category they fall into and outputting category to user
if bmi < 18.5: 
    print(f"BMI is: {str(bmi)}. You are underweight. Eat more homie.")
elif bmi < 25: 
    print(f"BMI is: {str(bmi)}. You have a normal weight. Stay this way.")
elif bmi < 30: 
    print(f"BMI is: {str(bmi)}. You are overweight. Maybe cutback for a bit.")
elif bmi < 35: 
    print(f"BMI is: {str(bmi)}. You are obese. Get help.")
else: 
    print(f"BMI is: {str(bmi)}. You are clinically obese. Get help.")