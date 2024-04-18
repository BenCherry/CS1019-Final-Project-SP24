# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:23:59 2024

@author: CherrBear
"""
import random


my_list1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
#my_list2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] 

my_2d_list = [
    [2, 3, 4, 5],
    [5, 4, 3 ,2],
    [2, 3, 4, 5],
    ]

        
card_index = random.randrange(len(my_list1)) # gets random index from list
drawn_card = my_list1.pop(card_index) # removes int from above index
print(drawn_card) # print test

player_hand = [] #creates empty player list to store cards 
dealer_hand = []

player_hand.append(drawn_card) # adds drawn_card to player hand (list)

while len(player_hand) != 2:
    card_index = random.randrange(len(my_list1))
    drawn_card = my_list1.pop(card_index)
    player_hand.append(drawn_card)
    
print(sum(player_hand))

def deal_hand(x): # gives the first 2 cards of the hand
    if len(x) == 0:       # argument is player_hand or dealer_hand READ THIS
        while len(x) != 2:
            card_index = random.randrange(len(my_list1))
            drawn_card = my_list1.pop(card_index)
            x.append(drawn_card)
        return x
            
def hit_or_stay(y): # determines if another card is drawn
    while y != 'h':
        if y == 's':
            break
        y = input('Enter a valid choice: ')
    return y
        
hand_signal = input('H to hit, S to stay: ') # argument for hit or stay func
hit_or_stay(hand_signal) # hit or stay func call with hand signal argument

def draw_card(x, y): # X is player or dealer, Y is hit or stay input
    if y == 'h':
        card_index = random.randrange(len(my_list1))
        drawn_card = my_list1.pop(card_index)
        x.append(drawn_card)
    hit_or_stay(hand_signal)
    return x

draw_card(player_hand, 'h')
print(sum(player_hand))
deal_hand(dealer_hand)   
    