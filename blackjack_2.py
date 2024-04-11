# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:09:54 2024

@author: CherrBear
"""
'''Should I make an if statement for entire player_hand sequence for
hand values of less than 17 for their first 2 cards, and an else statement for
values 17 - 20 to skip the draw sequence and move to the dealer?
The current program skips player print statements occasionaly. The console
shows the player initially had an 18, stored the value but didnt print, and 
then moved to the dealer sequence '''

import random

player_hand = ((random.randint(1, 10)) * 2)#gives player 2 cards
dealer_hand = ((random.randint(1, 10)) * 2)#gives dealer 2 cards

while player_hand <= 16:#gives the player a card until they have 17 or more
    player_hand += (random.randint(1, 10))#gives player another card
    if 17 <= player_hand <= 21:#stops giving cards when player has a hand
        print(f'You have {player_hand}, very nice!')
        #break
    elif player_hand > 21:#stops giving cards if they bust
        print(f'{player_hand}, you bust.')
    
    else:
        print(f'You have {player_hand}')#tells player what they have before taking another card
    
if 17 <= player_hand <= 21:#skips dealer turn if the player busts
    while dealer_hand <= 16:#gives dealer another card until he has a hand or busts
        print(f'{dealer_hand}, dealer hits.')
        dealer_hand += (random.randint(1, 10))#gives dealer another card
        if 17 <= dealer_hand <= 21:#stops dealer when he has a hand
            print(f'{dealer_hand}, dealer stays')
            #break
        elif dealer_hand >= 22:#stops the hand when dealer busts
                print(f'{dealer_hand}, dealer busts!')
else:
    print('Better luck next time loser.')#tell them how you really feel                

if player_hand > dealer_hand and player_hand <=21:
    print('You win, nice job!')
elif dealer_hand > player_hand and dealer_hand <= 21:
    print('lol')
elif player_hand == dealer_hand:
    print('It looks like we push')
print(player_hand)
print(dealer_hand)