# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 18:04:57 2024

@author: cherrbear
"""

import random

my_list1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11
            ] 
player_hand = [] #creates empty player list to store cards 
dealer_hand = []


#INPUT player_hand and dealer_hand lists as arguments
#PROCESSING random item removed from list, assigned to player/dealer list
#OUTPUT player or dealer list with the 2 random items
def deal_hand(hand): # 
    if len(hand) == 0:    
        for card in range(2): 
            card_index = random.randrange(len(my_list1))
            hand.append(my_list1.pop(card_index))
    return hand

#INPUT player/dealer_hand lists as arguments           
#PROCESSING checks for items in list, random item removed, assign to list
#OUTPUT adds random item to player/dealer, print statement if empty
def hit(x):
    if my_list1: # checks for items in list, 1 or more items it executes
        card_index = random.randrange(len(my_list1))
        x.append(my_list1.pop(card_index))
    else:
        print('Time to shuffle!')
    return x
        

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
#INPUT
#PROCESSING
#OUTPUT
def house_hand():
    if sum(dealer_hand) < 17:
        while sum(dealer_hand) < 17:
            hit(dealer_hand)
            print(f'Dealer has {sum(dealer_hand)}')
    elif sum(dealer_hand) > 21:
        print(f'Dealer busts with {sum(dealer_hand)}')        

#INPUT
#PROCESSING
#OUTPUT
def winning_hand():
    if sum(dealer_hand) > sum(player_hand):
        print(f'You have a {sum(player_hand)}, ' 
              f'dealer has a {sum(dealer_hand)}, dealer wins.')
    elif sum(dealer_hand) < sum(player_hand):
        print(f'Dealer has a {sum(dealer_hand)}, '
              f' you win with a {sum(player_hand)}')
    elif sum(dealer_hand) == sum(player_hand):
        print("A push is a win")

start_game()
