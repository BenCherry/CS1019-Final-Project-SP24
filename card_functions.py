# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 20:25:14 2024

@author: cherrbear


Spring 2024 Intro to Programming w/ Python Term Project


Functions dealing with removing cards from the card list and
putting them in the player_hand and dealer_hand lists, and comparing
the total value of the player_hand and dealer_hand lists to determine
if the Dealer will draw again, and the outcome of the hand
"""

import random

#INPUT player_hand and dealer_hand lists as arguments
#PROCESSING random item removed from list, assigned to player/dealer list
#OUTPUT player or dealer list with the 2 random items
def deal_hand(hand): 
    """ 
    Starts the hand giving 2 cards.
    
    Args:
        a (list): The empty player or dealer_hand list.
        
    Returns:
        list: List with 2 random values from my_list1.
    """
    if len(hand) == 0:    
        for card in range(2): 
            card_index = random.randrange(len(my_list1))
            hand.append(my_list1.pop(card_index))
    return hand

#INPUT player/dealer_hand lists as arguments           
#PROCESSING checks for items in list, random item removed, assign to list
#OUTPUT adds random item to player/dealer, print statement if empty
def hit(x):
    """"
    Draws a random 'card' from my_list1 and adds it to player/dealer list.
        
    Args:
        a (list): player / dealer_hand list.
        
    Returns:
        list: Value from my_list1 appended to player/dealer list.
    """
    if my_list1: # checks for items in list, 1 or more items it executes
        card_index = random.randrange(len(my_list1))
        x.append(my_list1.pop(card_index))
    else:
        print('Time to shuffle!')
    return x

#INPUT
#PROCESSING
#OUTPUT
def house_hand():
    """
    Determines if the dealer draws more cards or stays.

    Args:
        a (none) None.
        
    Returns:
        list: Finished dealer_hand list.
    """
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
    """
    Compares the hands and returns the result (win / lose/ push).

    Args:
        a (none): None.
        
    Returns:
        str: Prints the winner.
    """
    if sum(dealer_hand) > sum(player_hand):
        print(f'You have a {sum(player_hand)}, ' 
              f'dealer has a {sum(dealer_hand)}, dealer wins.')
    elif sum(dealer_hand) < sum(player_hand):
        print(f'Dealer has a {sum(dealer_hand)}, '
              f' you win with a {sum(player_hand)}')
    elif sum(dealer_hand) == sum(player_hand):
        print("A push is a win")
