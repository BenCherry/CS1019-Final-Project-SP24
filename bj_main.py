# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 18:04:57 2024

@author: cherrbear

Contains the list of cards, the Player and Dealer lists,
and the function to start the game

***Make sure to import your other files***
"""

import card_functions

my_list1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11
            ] 
player_hand = [] #creates empty player list to store cards 
dealer_hand = []


#INPUT no arguments, starts game when called
#PROCESSING calls deal_hand func, infinite loop, 
#OUTPUT 
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
    
    house_hand()
    winning_hand()

start_game()
