# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 19:04:30 2024

@author: cherrbear
"""

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

#PLAYER HAND

player_card1 = ((random.randint(1, 11)))#players 1st card
player_card2 = 0#intialize 2nd card to be used below
if player_card1 == 11:#if the player has an ACE, do this
    player_card2 = ((random.randint(1, 10)))#players 2nd card if up card == 11
    if player_card1 + player_card2 == 21:#if player has blackjack, do this / need to check if player == dealer
        print('Blackjack!')
elif player_card1 == 10:#if the player has a 10 value card, do this
    player_card2 = ((random.randint(1, 11)))#player 2nd card
    if player_card1 + player_card2 == 21:#if player has blackjack, do this
        print('Blackjack!')
else:#if the player doesnt have an ACE or 10 value, do this
    player_card2 = ((random.randint(1, 11)))
    

player_hand = (player_card1#add players 2 cards together
               + player_card2)


#*********************************************************************************************************

#DEALER HAND
dealer_up_card = ((random.randint(1, 11)))

print(f'{dealer_up_card} --> d1')#print test for dealers first card / need functionality for an ACE (11)
dealer_hole_card = 0#initialize dealer hole card to be used below
if dealer_up_card == 11:#if up card is  an ACE, do this
    (dealer_hole_card := ((random.randint(1, 10))))
    print('Would you like insurance?')#need to implement an insurance function
    if dealer_hole_card == 10:#if up card==ACE and hole card is 10, do this
        print('Dealer backjack')#declares BJ if first card is 11 2nd is 10 --> ADD if up card is 11 offer insurance
    

elif dealer_up_card == 10 and dealer_hole_card == 11:#if dealer has 10 up and an ACE, auto win/push
    print('Dealer blackjack')
else:
    (dealer_hole_card := ((random.randint(1, 11))))#if up card != 10 or 11, do this 
    

dealer_hand = (dealer_up_card
               + dealer_hole_card)#adds dealers  2 cards together
    
#dealer_hand = ((random.randint(1, 10)) * 2)#gives dealer 2 cards
#*********************************************************************************************************


#PLAYER HIT SEQUENCE
if player_hand <= 16:

    while player_hand <= 16:#gives the player a card until they have 17 or more
    
        player_hand += (random.randint(1, 10))#gives player another card
        if 17 <= player_hand <= 21:#stops giving cards when player has a hand
            print(f'You have {player_hand}, very nice!')
        
        elif player_hand > 21:#stops giving cards if they bust
            print(f'{player_hand}, you bust.')
            
        else:
            print(f'You have {player_hand}')#tells player what they have before taking another card
            
else:
    print(f'You have {player_hand}')

#************************************************************************
#DEALER HIT SEQUENCE

if 17 <= player_hand <= 21:#skips dealer turn if the player busts
    while dealer_hand <= 16:#gives dealer another card until he has a hand or busts
        print(f'{dealer_hand}, dealer hits.')
        dealer_hand += (random.randint(1, 10))#gives dealer another card
        
        if 17 <= dealer_hand <= 21:#stops dealer when he has a hand
            print(f'{dealer_hand}, dealer stays')
            
        elif dealer_hand >= 22:#stops the hand when dealer busts
                print(f'{dealer_hand}, dealer busts!')
else:
    print('Better luck next time loser.')#tell them how you really feel                

if player_hand > dealer_hand and player_hand <= 21:
    #print(f'dealer has {dealer_hand}')
    print('You win, nice job!')
elif dealer_hand > player_hand and dealer_hand <= 21:
    #print(f'dealer has {dealer_hand}')
    print('lol')
elif player_hand == dealer_hand:
    print('it looks like we push')


print(player_hand)
print(dealer_hand)