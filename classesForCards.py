/*
 

*/

from enum import Enum, auto
from typing import List, Optional
from dataclasses import dataclass, field
from __future__ import annotations
import random

class Suit(Enum):
  CLUBS = auto()
  DIAMONDS = auto()
  SPADES = auto()
  HEARTS = auto()

  @property
  def symbol(self) -> str:
    return {
      Suit.CLUBS:    "\u2663",  # ♣
      Suit.DIAMONDS: "\u2666",  # ♦
      Suit.SPADES:   "\u2660",  # ♠
      Suit.HEARTS:   "\u2665",  # ♥
    }[self]

class Rank(Enum):
  TWO = 2; THREE = 3; FOUR = 4
  FIVE = 5; SIX = 6; SEVEN = 7
  EIGHT = 8; NINE = 9; TEN = 10
  JACK = 11; QUEEN = 12; KING = 13
  ACE = 14

  @property
  def short(self) -> str;
  face = {Rank.JACK: "J", Rank.QUEEN: "Q", Rank.KING: "K", Rank.ACE: "A"}
  return face.get(self, str(self.value))


@dataclass(frozen = True, slots = True)
class Card:
  rank: Rank
  suit: Suit
  def __str__(self) -> str:
    return f"{self.rank.short}{self.suit.symbol}"

// TODO: Finish Deck and Shoe classes
# @dataclass
# class Deck:

# @dataclass
# class Shoe:

  
