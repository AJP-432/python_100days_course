
# Introducing program
print("This is a leap year calculator.")

# Asking for input for year to check 
year = int(input("Which year do you want to check: "))

# Checking if year is leap and outputting anwser. Methodolgy used is below

if year % 4 == 0: 
    if year % 100 == 0: 
        if year % 400 == 0: 
            print(f"{str(year)} is a leap year.")
            
        else: print(f"{str(year)} is not a leap year.")
    
    else: 
        print(f"{str(year)} is a leap year.")
    
else: 
    print(f"{str(year)} is not a leap year.")
    
# From Microsoft: https://docs.microsoft.com/en-us/office/troubleshoot/excel/determine-a-leap-year   
 
# To determine whether a year is a leap year, follow these steps:

# If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
# If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
# If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
# The year is a leap year (it has 366 days).
# The year is not a leap year (it has 365 days).
