# Intro game
print("Welcome to Treasure Island. Your mission is to find the treasure!")

print(''' 
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************      
      ''')

# Asking to go left or right, right leads to winning
left_right = input("Do you wanna go left or right? (left/right)\n").lower()

if left_right == "right":
    print("You step into a bear trap and, over a few hours, bleed out. GAME OVER!")
    quit()

# Asking whether to swim or wait, waiting leads to winning
wait_swim = input("You see an island out from the beach. Should you swim to it or wait? (swim/wait)\n").lower()

if wait_swim == "swim": 
    print("You attempt to swim only to be mauled by sharks. GAME OVER!")
    quit()

print("A sailor comes by and takes you to the island for free. Awesome.")
        
# Asking for which box to open, yellow leads to winning
yellow_red_blue = input("You find 3 treasures boxes. Which box should you open? red, blue, or yellow? (red/blue/yellow)\n").lower()

if yellow_red_blue == "red":
    print("You open the box to find snakes! You are attacked and killed. GAME OVER!")
elif yellow_red_blue == "blue":
    print("You open the box only to unleash poisonous gas! You instantly faint and die unconciously in minutes. GAME OVER!")
else: 
    print("You open the box to find gold! You have found the treasure. WINNER!")