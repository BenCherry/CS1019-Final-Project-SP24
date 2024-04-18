# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 09:19:06 2024

@author: cherrbear
"""
import random

play_hand = input('press Y to play, any key to leave: ')

def play_blackjack(y_to_play):
    if y_to_play != 'y':
        print('thank you for playing')
    else:
        print('Lets play!')
        player_bet = y_to_play
        return player_bet
play_blackjack(play_hand)

playing_hand = play_blackjack(play_hand)

def player_bet(playing_hand):
    bet_hand = int(input('How much bet?: '))
    return bet_hand

