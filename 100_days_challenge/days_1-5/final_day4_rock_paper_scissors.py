# Setting up art
# Rock
rock_art = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper_art = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors_art = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# All arts in art array
art = [rock_art, paper_art, scissors_art]

import random
# Introducing program and prompting user input
print("This is a rock, paper, and scissors game against the computer. Which do you choose? ")
human_choice = int(input("Type 0 for Rock, 1 for Paper, and 2 for Scissors: "))
# Generating computer's choice
pc_choice = random.randint(0, 2)
if human_choice == 2:
    print("HI")
# Logic for who wins and printing respectively
if human_choice is (not 0 or 1 or 2):
    print("Invalid response. You LOSE!")
    
elif human_choice == pc_choice:
    print(f"You chose:\n{art[human_choice]}\nComputer chose:\n{art[pc_choice]}\nIt is a DRAW.")
    
elif human_choice == 0 and pc_choice == 1: 
    print(f"You chose:\n{art[human_choice]}\nComputer chose:\n{art[pc_choice]}\nComputer WINS. You LOSE.")
    
elif human_choice == 0 and pc_choice == 2: 
    print(f"You chose:\n{art[human_choice]}\nComputer chose:\n{art[pc_choice]}\nYou WIN.")
    
elif human_choice == 1 and pc_choice == 0: 
    print(f"You chose:\n{art[human_choice]}\nComputer chose:\n{art[pc_choice]}\nYou WIN.")
    
elif human_choice == 1 and pc_choice == 2: 
    print(f"You chose:\n{art[human_choice]}\nComputer chose:\n{art[pc_choice]}\nComputer WINS. You LOSE.")
    
elif human_choice == 2 and pc_choice == 0: 
    print(f"You chose:\n{art[human_choice]}\nComputer chose:\n{art[pc_choice]}\nComputer WINS. You LOSE.")
    
else: 
    print(f"You chose:\n{art[human_choice]}\nComputer chose:\n{art[pc_choice]}\nYou WIN.")
