# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 09:19:06 2024

@author: cherrbear
"""
play_hand = input('press Y to play, any key to leave: ')

def play_blackjack(y_to_play):
    if y_to_play != 'y':
        print('thank you for playing')
        #break
    else:
        print('Lets play!')
        return y_to_play
    
       
        
play_blackjack(play_hand)   
    
