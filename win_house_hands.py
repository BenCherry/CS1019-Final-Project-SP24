# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 20:25:14 2024

@author: cherrbear
"""
       
def house_hand():
    if sum(dealer_hand) < 17:
        while sum(dealer_hand) < 17:
            hit(dealer_hand)
            print(f'Dealer has {sum(dealer_hand)}')
    elif sum(dealer_hand) > 21:
        print(f'Dealer busts with {sum(dealer_hand)}')        

def winning_hand():
    if sum(dealer_hand) > sum(player_hand):
        print(f'You have a {sum(player_hand)}, ' 
              f'dealer has a {sum(dealer_hand)}, dealer wins.')
    elif sum(dealer_hand) < sum(player_hand):
        print(f'Dealer has a {sum(dealer_hand)}, '
              f' you win with a {sum(player_hand)}')
    elif sum(dealer_hand) == sum(player_hand):
        print("A push is a win")