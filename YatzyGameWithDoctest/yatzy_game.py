
import random


def roll(number_of_dice=5):
    """
    Roll the indicated number of 6 sided dice using a random number generator

    >>> random.seed(1234)
    >>> roll(5)
    [1, 1, 1, 4, 5]
    """
    return sorted(random.choice((1, 2, 3, 4, 5, 6))
                  for i in range(number_of_dice))