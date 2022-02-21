# Asking for age and calculating years left assuming they die at 90
years_left = 90 - int(input("What is your age: "))

# Calculating how many days, weeks, and months their years left equal to
days_left, weeks_left, months_left = years_left * 365, years_left * 52, years_left * 12

# Printing amount of days/weeks/months left
print(f"You have {days_left} days/{weeks_left} weeks/{months_left} months left to live.")