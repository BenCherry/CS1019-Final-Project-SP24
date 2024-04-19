# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 18:04:57 2024

@author: cherrbear
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:23:59 2024

@author: CherrBear
"""
import random

my_list1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] 
player_hand = [] #creates empty player list to store cards 
dealer_hand = []

def deal_hand(hand): # gives the first 2 cards of the hand
    if len(hand) == 0:    
        for card in range(2):      # argument is player_hand or dealer_hand RE
            card_index = random.randrange(len(my_list1))
            hand.append(my_list1.pop(card_index))
    return hand
            
def hit(x):
    if my_list1:
        card_index = random.randrange(len(my_list1))
        x.append(my_list1.pop(card_index))
    else:
        print('Time to shuffle!')
    return x
        

def start_game():
    play = input("Pres 'Y' to play, or 'Q' to exit: ")
    if play == 'y':
        deal_hand(player_hand)
        deal_hand(dealer_hand)
        
        print(f'Dealer shows {sum(dealer_hand)}, you have: {sum(player_hand)}')
        while True: # infinite loop, runs until break
            hit_stay = input("Press 'H' to hit, or 'S' to stay: ")
            if hit_stay == 'h':
                hit(player_hand)
                print(f"You have: {sum(player_hand)}")
                if sum(player_hand) > 21:
                    print(f'You bust with {sum(player_hand)}')
                    break
            elif hit_stay == 's':
                print(f'You stay with {sum(player_hand)}.')
                break
            else:
                print('Enter a valid choice: ')
                
    elif play == 'q':
        print('Thanks for stopping in!')
