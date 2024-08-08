# -*- coding: utf-8 -*-
"""
Created on Sat May  4 13:32:57 2024

@author: cherrbear  Ryan Cherry

Main function that runs the program.

This is a blackjack simulator that allows the user to play single deck blackjack.
My goal was to match the programs logic to the actual procedures and flow of a
real blackjack game.

"""


from start import start_game


def main():
    """
    Main function that runs the program.

    Args:
        None.

    Returns:
        None.
    """

    user_start = ' '

    while user_start not in ['P', 'Q']:
        user_start = input('\nPress P to play, or Q to quit: \n')
        if user_start.upper() == 'P':
            print('\nLet\'s play!\n')
            start_game()
        elif user_start.upper() == 'Q':
            print('Exiting\n')
            break

        else:
            print('Enter a valid choice.\n')


if __name__ == '__main__':
    main()
