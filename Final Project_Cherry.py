# -*- coding: utf-8 -*-
"""
Created on Sat May  4 13:32:57 2024

@author: cherrbear  Ryan Cherry

Main function that runs the program.

This is a blakjack simulator that allows the user to play single deck 
blackjack.

Cards are randomly drawn from a deck , and added to the player and dealer lists.

Aces are handled by checking the sum of the player/dealer list, and if over 21,
and an Ace (11) is present in the list, subtracting 10 and saving the value to
a local variable as the score. This solves the issue of an Ace being counted as
an 11 or a 1, whichever is more beneficial.

Storing the score this way allows for multiple aces (a list total over 21).

Scores are then compared and the result is output.

Cards are then collected and moved to the discard, or shuffled as required.

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
