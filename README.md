# CS1019 Term Project SP2024

A console-based blackjack game 


This is a blackjack simulator that allows the user to play single deck 
blackjack.

Cards are randomly drawn from a deck , and added to the player and dealer lists.

Aces are handled by checking the sum of the player/dealer list, and if over 21,
and an Ace (11) is present in the list, subtracting 10 and saving the value to
a local variable as the score. This solves the issue of an Ace being counted as
an 11 or a 1, whichever is more beneficial.

Storing the score this way allows for multiple aces (a list total over 21).

Scores are then compared and the result is output.

Cards are then collected and moved to the discard, or shuffled as required.
