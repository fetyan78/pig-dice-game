import random

class Dice:
    """class for a six dice"""

    def __init__(self):
        """initialize the dice"""
        self.sides = [1, 2, 3, 4, 5, 6]
        random.shuffle(self.sides)
    
    def roll(self):
        """roll the dice"""
        roll1 = random.choice(self.sides)
        roll2 = random.choice(self.sides)
        total = roll1 + roll2
        return {'rolls': (roll1, roll2), 'total': total}