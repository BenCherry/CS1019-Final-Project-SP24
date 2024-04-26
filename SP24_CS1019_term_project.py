# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:11:50 2024

@author: cherrbear
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 14:52:56 2024

@author: CherrBear
"""

import random


my_list1 = [
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11
]
player_hand = []  # creates empty player list to store cards
dealer_hand = []


def deal_hand(hand): 
    """
    Start the hand giving 2 cards.

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


def hit(player_or_dealer):
    """"
    Draws a random 'card' from my_list1 and adds it to player/dealer list.
        
    Args:
        a (list): player / dealer_hand list.
        
    Returns:
        list: Value from my_list1 appended to player/dealer list.
    """
    if my_list1: # checks for items in list, 1 or more items it executes
        card_index = random.randrange(len(my_list1))
        player_or_dealer.append(my_list1.pop(card_index))
    else:
        print('Time to shuffle!')
    return player_or_dealer


def player(player_hand):
    while sum(player_hand) < 21:
        hand_signal = input('Press "H" to hit, or any key to stay: \n')
        if hand_signal == 'h':
            hit(player_hand)
            print(f'You have: {sum(player_hand)}\n')
            if player_count() == True:
                break
        elif hand_signal != 'h':
            print(f'You stay with {sum(player_hand)}\n')
            break
        else:
            break

        
        
def player_count():  # FIXME Only returns False
    bust = False
    if sum(player_hand) > 21:
        bust = True        
    return bust




def house_hand():
    """
    Determine if the dealer draws more cards or stays.

    Args:
        a (none) None.
        
    Return:
        list: Finished dealer_hand list.
    """

    while sum(dealer_hand) < 17:
        print(f'')
        hit(dealer_hand)
        if dealer_count() == True:
            print('house_hand True test') # 


def dealer_count():
    bust = False
    if sum(dealer_hand) > 21:
        bust = True
    return bust




def winning_hand():
    """
    Compares the hands and returns the result (win / lose/ push).

    Args:
        a (none): None.
        
    Returns:
        str: Prints the winner.
    """
    if dealer_count() == True:
        print(f'Dealer busts with:{sum(dealer_hand)}\n'
              f'Player wins with: {sum(player_hand)}')
    elif player_count() == True:
        print(f'You bust with a: {sum(player_hand)}\n'
              f'Dealer has: {sum(dealer_hand)}')
    
    
    
    elif sum(dealer_hand) < sum(player_hand):
        print(f'Dealer has a {sum(dealer_hand)}, '
              f' you win with a {sum(player_hand)}\n')
    elif sum(dealer_hand) == sum(player_hand):
        print("A push is a win\n")

deal_hand(player_hand)
print(f'You have: {sum(player_hand)}\n')
deal_hand(dealer_hand) 
print(f'Dealer shows: {sum(dealer_hand)}\n')
player(player_hand)
house_hand()   
winning_hand()
# Need to add check in winning_hand() whether player/dealer_count for true 
# To end hand