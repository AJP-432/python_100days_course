# Declaring bill variable 
bill = 0

# Asking for height
height = int(input("What is your height in cm: "))

# Can ride coaster if taller or equal to 120 cm
if height >= 120:
    print("You can ride the rollercoaster!")
    
    # Asking for age to determine ticket price
    age = int(input("What is your age: "))
    
    # Determining ticket price depending on age
    if age < 12:
        print("Child tickets are $5") 
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7") 
        bill = 7
    else: 
        print("Adult tickets are $12") 
        bill = 12
    
    # Asking if they want a photo
    wants_photo = input("Do you want a photo taken? (y/n) ")
    
    # If they want photo, then pay $3 extra
    if wants_photo == "y": 
        bill += 3

    print(f"Your final bill is ${bill}")
            
# if not tall enough, telling them to come back later
else: 
    print("Sorry, you must grow taller before you can ride. It is for your own safety, otherwise you will die")