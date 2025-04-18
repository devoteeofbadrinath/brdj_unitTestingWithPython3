
import random

from yatzy import *


def play_yatzy():
    """
    Play an interactive game of Yatzy on the command line
    """
    available_categories = [yatzy, full_house, four_of_a_kind, three_of_a_kind, two_pairs,
                            small_straight, large_straight,
                            ones, twos, threes, fours, fives, sixes,
                            chance]
    play_yatzy_with_categories(available_categories)


def play_yatzy_with_categories(available_categories, input_source=input):
    """
    Play an interactive game of Yatzy on the command line,
    with only the given categories available

    :para, available_categories: list of category functions.
    Each function takes a list of dice integers, and returns an integer score

    """


def roll(number_of_dice=5):
    """
    Roll the indicated number of 6 sided dice using a random number generator

    >>> random.seed(1234)
    >>> roll(5)
    [1, 1, 1, 4, 5]
    """
    return sorted(random.choice((1, 2, 3, 4, 5, 6))
                  for i in range(number_of_dice))