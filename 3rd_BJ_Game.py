# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 14:52:56 2024

@author: CherrBear
"""
import random
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
def house_hand():
    """
    Determine if the dealer draws more cards or stays.

    Args:
        a (none) None.
        
    Return:
        list: Finished dealer_hand list.
    """
    if players_count != True:
        if sum(dealer_hand) < 17:
            while sum(dealer_hand) < 17:
                hit(dealer_hand)
                print(f'Dealer has {sum(dealer_hand)}')
        elif sum(dealer_hand) > 21:
            print(f'Dealer busts with {sum(dealer_hand)}')


my_list1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11
] 
player_hand = []  # creates empty player list to store cards
dealer_hand = []
       


def player():
    while sum(player_hand) < 21:
        print(f'You have: {sum(player_hand)}')
        hand_signal = input('h to hit, any key to stay: ')
        if hand_signal == 'h':
            hit(player_hand)
        elif hand_signal != 'h':
            print(f'You stay with {sum(player_hand)}')
            break
        else:
            break
        #if sum(player_hand) > 21:
            #print(f'You bust with {sum(player_hand)}')
        
        
def player_count():
    if sum(player_hand) > 21:
        print(f'You bust with {sum(player_hand)}')
    return True
players_count = player_count   
print(players_count)    

def dealer_count():
    if sum(dealer_hand) > 21:
        print(f'Dealer busts with: {sum(dealer_hand)}')
    return True
dealers_count = dealer_count()
#print(f'Dealer: {sum(dealer_hand)} \nPlayer: {sum(player_hand)}')

deal_hand(player_hand)
deal_hand(dealer_hand) 
player()
player_count()
house_hand()   
winning_hand()
# Need to add check in winning_hand() whether player/dealer_count for true 
# To end hand