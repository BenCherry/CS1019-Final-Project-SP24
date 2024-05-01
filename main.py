# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 12:43:12 2024.

@author: CherrBear

SPRING 2024 CS1019 TERM PROJECT

MAIN FILE

"""


from start import start_game


def main():
    """
    Main function that runs the program.

    Returns
    -------
    None.

    """

    user_start = ' '

    while user_start not in ['P', 'Q']:
        user_start = input('Press P to play, or Q to quit: \n\n')
        if user_start.upper() == 'P':
            print('Let\'s play!\n\n')
            start_game()
        elif user_start.upper() == 'Q':
            print('Exiting\n\n')
            break

        else:
            print('Enter a valid choice.\n\n')


if __name__ == '__main__':
    main()
