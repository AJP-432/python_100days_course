# Introducting program
print("Welcome to the love calculator based on the Buzzfeed method.")

# Asking for user and their crushes name, applying lower method, and saving to variable
name1 = input("What is your name?\n").lower()
name2 = input("What is their name?\n").lower()

# Initiating variable for  number of times the letters of TRUE and LOVE occur in their names 
true_letters_count = 0
love_letters_count = 0

# Putting together names for effeciency
combined_name = name1 + name2

# Counting combined occurences with count menthod and adding into respective variables 
true_letters_count = combined_name.count("t") + combined_name.count("r") + combined_name.count("u") + combined_name.count("e")
love_letters_count = combined_name.count("l") + combined_name.count("o") + combined_name.count("v") + combined_name.count("e")

# Putting digits together into final love percentage
final_result = str(true_letters_count) + str(love_letters_count)

# Outputting percentage amount
print(f"You guys have scored {final_result}%.")

# Telling what their results mean
if int(final_result) < 10 or int(final_result) > 90: 
    print("You go together like coke and mentos!")
    
elif int(final_result) > 40 and int(final_result) < 50: 
    print("You guys are alright.")
    
else: 
    print("Idek m8.")

