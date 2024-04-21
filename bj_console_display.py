# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 15:45:19 2024

@author: cherrbear


Spring 2024 Intro to Programming w/ Python Term Project


The following is formatting for the output of the blackjack game
in the console.



"""

user_name = input('Enter your name: ').strip().lower().title()
score = 100 # These need counters to keep track made
hands_won = 100 #
hands_lost = 100 #
dealer_bjs = 15
player_bjs = 20
pushes = 7


def console_interface():
    """
    Displays the interface for the player in the console and the game stats.
    
    Args: Will be game stats.
        a (int): The score.
        b (int):The hands won.
        c (int): Etc...
            
    Returns:
        (type): Display game in the console.
    """
    
print(f'\nHands Played: {score:<5} ' # Displays hands won/ lost/ played
      f'Hands Won: {hands_won:<5} '
      f'Hands Lost: {hands_lost:<5} '
      f'Pushes: {pushes:<5} '
      f'\n\nDealer Blackjacks: {dealer_bjs:<5} '
      f'{user_name:<} Blackjacks: {player_bjs:<5}')




