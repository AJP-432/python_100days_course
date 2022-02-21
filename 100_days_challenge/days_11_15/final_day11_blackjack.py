# Ajlal Paracha June 1, 2021
# This is Blackjack -- Enjoy!
# Because of recursion, when win or loss outcome is reached, it may be printed multiple times
# Things to add: Split, other players, UI improvements

import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

# Assumptions: 
# Deck is unlimited, no jokers, jack/queen/king = 10, ace = 1 or 11, all cards have equal probability (even if they are already drawn) i.e. not removed 
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(): 
    """Picks random card from deck"""
    return random.choice(deck)

def game():
    """Blackjack Game"""
    # Checking if 11 to 1 ace conversion is needed to avoid printing scores above 21
    if sum(user_hand) > 21 and 11 in user_hand: 
        user_hand[user_hand.index(11)] = 1
        
    print(f"Your hand: {user_hand} -- Current score {sum(user_hand)}\nComputer first card: {pc_hand[0]}.")
    
    # looping through hit and hold logic
    while True: 
        # Checking for Blackjacks
        if sum(user_hand) == 21:
            print("You have Blackjack -- Congratulations, you win 😁!")
            print(f"Computer hand: {pc_hand}, total {sum(pc_hand)}")
            return
        elif sum(pc_hand) == 21:
            print("The computer has Blackjack -- You lose 😭!")
            print(f"Computer hand: {pc_hand}, total {sum(pc_hand)}")
            return
                
        else: 
            # Checking if user busted and if they have ace and changing ace value from 11 to 1
            if sum(user_hand) > 21 and 11 in user_hand: 
                user_hand[user_hand.index(11)] = 1
            
            elif sum(user_hand) > 21:
                print("You have busted -- You lose 😭!")
                print(f"Your hand: {user_hand}, total {sum(user_hand)}")
                print(f"Computer hand: {pc_hand}, total {sum(pc_hand)}")
                return
            
            else:
                # Asking for hit or hold and doing accordingly
                hit_hold_choice = input("Hit? (y/n)\n").lower()
                
                if hit_hold_choice == "y":
                    user_hand.append(deal_card())
                    game()
                
                elif hit_hold_choice == "n":
                    # computer drawing cards while its hand is under 17 
                    while sum(pc_hand) < 17: 
                        pc_hand.append(deal_card())
                        if sum(user_hand) > 21 and 11 in user_hand: 
                            pc_hand[pc_hand.index(11)] = 1
                    # if computer busts while drawing
                    if sum(pc_hand) > 21: 
                        print("They have busted, you win 😁!")
                        print(f"Your hand: {user_hand}, total {sum(user_hand)}")
                        print(f"Computer hand: {pc_hand}, total {sum(pc_hand)}")
                        return
                        
                    else: 
                        # Comparing user and computers scores and printing accordingly
                        if sum(user_hand) > sum(pc_hand):
                            print("You are closer to 21 -- You win 😁!")
                            print(f"Your hand: {user_hand}, total {sum(user_hand)}")
                            print(f"Computer hand: {pc_hand}, total {sum(pc_hand)}")
                            return
                            
                        elif sum(user_hand) < sum(pc_hand): 
                            print("The computer is closer to 21 -- You lose 😭!")
                            print(f"Your hand: {user_hand}, total {sum(user_hand)}")
                            print(f"Computer hand: {pc_hand}, total {sum(pc_hand)}")
                            return
                        
                        else: 
                            print("It's a draw 💤")
                            print(f"Your hand: {user_hand}, total {sum(user_hand)}")
                            print(f"Computer hand: {pc_hand}, total {sum(pc_hand)}")
                            return
                        
                else: 
                    print("You just do not want to get along using invalid inputs...Well I'm NOT PLAYING ANYMORE") 
                    quit()


while True: 
       
    print(logo)
    choice = input("Would you like to play? (y/n)\n").lower()
    
    # Clearing screen
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
    
    if choice == "y":
        # Initating/Resetting hands by populating with random cards
        user_hand, pc_hand = [], []
        for _ in range(2): 
            user_hand.append(deal_card())
            pc_hand.append(deal_card())
        game()
        
    elif choice == "n": 
        print("Have a nice day!")
        break
    
    else: 
        print("Invalid input. If you won't follow the rules, neither will I. Get out of here 😡!")
        break