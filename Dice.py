import random

class Dice:
    """class for a six dice"""

    def __init__(self):
        """initialize the dice"""
        self.sides = [1, 2, 3, 4, 5, 6]
        random.shuffle(self.sides)