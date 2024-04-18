# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:23:59 2024

@author: CherrBear
"""
import random


my_list1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
my_list2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]



        
card_index = random.randrange(len(my_list1)) # gets random index from list
drawn_card = my_list1.pop(card_index) # removes int from above index
print(drawn_card)

player_hand = [] #creates empty player list to store 
dealer_hand = []

player_hand.append(drawn_card) # adds drawn_card to player hand (list)


def draw_card():
    pass
    