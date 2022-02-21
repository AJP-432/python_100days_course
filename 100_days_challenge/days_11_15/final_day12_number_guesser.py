# Ajlal Paracha June 21, 2021
# This is a number guessing game with 10 or 5 levels on easy and hard difficulties, respectively, and a range of 1-100; Enjoy!

import random

# Title and intro to program
print("""                                                                                                                                                              
         ,--.                                                                                                                                                 
       ,--.'|                       ____                                         ,----..                                                                      
   ,--,:  : |                     ,'  , `.  ,---,                               /   /   \                                                                     
,`--.'`|  ' :         ,--,     ,-+-,.' _ |,---.'|               __  ,-.        |   :     :          ,--,                                              __  ,-. 
|   :  :  | |       ,'_ /|  ,-+-. ;   , |||   | :             ,' ,'/ /|        .   |  ;. /        ,'_ /|             .--.--.    .--.--.             ,' ,'/ /| 
:   |   \ | :  .--. |  | : ,--.'|'   |  ||:   : :      ,---.  '  | |' |        .   ; /--`    .--. |  | :    ,---.   /  /    '  /  /    '     ,---.  '  | |' | 
|   : '  '; |,'_ /| :  . ||   |  ,', |  |,:     |,-.  /     \ |  |   ,'        ;   | ;  __ ,'_ /| :  . |   /     \ |  :  /`./ |  :  /`./    /     \ |  |   ,' 
'   ' ;.    ;|  ' | |  . .|   | /  | |--' |   : '  | /    /  |'  :  /          |   : |.' .'|  ' | |  . .  /    /  ||  :  ;_   |  :  ;_     /    /  |'  :  /   
|   | | \   ||  | ' |  | ||   : |  | ,    |   |  / :.    ' / ||  | '           .   | '_.' :|  | ' |  | | .    ' / | \  \    `. \  \    `. .    ' / ||  | '    
'   : |  ; .':  | : ;  ; ||   : |  |/     '   : |: |'   ;   /|;  : |           '   ; : \  |:  | : ;  ; | '   ;   /|  `----.   \ `----.   \'   ;   /|;  : |    
|   | '`--'  '  :  `--'   \   | |`-'      |   | '/ :'   |  / ||  , ;           '   | '/  .''  :  `--'   \'   |  / | /  /`--'  //  /`--'  /'   |  / ||  , ;    
'   : |      :  ,      .-./   ;/          |   :    ||   :    | ---'            |   :    /  :  ,      .-./|   :    |'--'.     /'--'.     / |   :    | ---'     
;   |.'       `--`----'   '---'           /    \  /  \   \  /                   \   \ .'    `--`----'     \   \  /   `--'---'   `--'---'   \   \  /           
'---'                                     `-'----'    `----'                     `---`                     `----'                           `----'             
      """)
print("Welcome to the Number Guessing Game!")


def play_game():    
    number_to_guess = random.randint(1, 100)
    
    # Gaining valid difficulty level input
    while True: 
        
        difficulty = input("Choose a difficulty. Type \"Easy\" or \"Hard\": ").lower()
        
        if difficulty == "easy" or difficulty == "hard":
            break
        else: 
            print("Invalid. Try again")
        
    if difficulty == "easy": 
        lives = 10
    
    else:
        lives = 5
        
    print(f"You have {lives} lives remaining.")
    
    while lives != 0: 
        
        #Gaining valid int input for number
        while True: 
            
            guess = int(input("Make a guess: "))

            if type(guess) is int:
                break
            
            else:
                print("Inavlid. Integers only. Try again.")
        
        # If guess is correct 
        if guess == number_to_guess: 
            global win
            win = True
            break
        
        # If guess is too high
        elif guess > number_to_guess: 
            lives -= 1
            print(f"Too high.\nGuess again.\nYou have {lives} lives remaining.")
           
        # If guess is too low    
        else: 
            lives -= 1
            print(f"Too low.\nGuess again.\nYou have {lives} lives remaining.")
    
    if win: 
        print(f"Correct!. The number was {number_to_guess}.")
    
    else: 
        print(f"You are out of lives. The number was {number_to_guess}. Better luck next time!")
            
while True: 
    win = False
    play_game()
    
    while True: 
        play_again = input("Would you like to play again? (y/n) ").lower()
        
        if play_again == "y" or play_again == "n":
            break
        
        else: 
            print("Invalid. Try again.")
    
    if play_again == "n":
        print("Have a nice day!")
        exit()
    
    