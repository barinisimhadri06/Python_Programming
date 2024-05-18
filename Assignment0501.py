# Author: Barini Simhadri
# Date: 13-02-2024
# Honor Statement: "I have not given or received any unauthorized assistance on this assignment."
# link:https://youtu.be/xhx3s1_ejdg

import random

class SixSideDie():
    """Class representing a six-sided die."""

    def __init__(self):
        """Initialize the six-sided die."""
        self.sides = 6
        self.face_value = int()

    def roll(self):
        """Simulate rolling the six-sided die and return the result."""
        self.face_value = random.randint(1, self.sides)
        return self.face_value

    def getFaceValue(self):
        """Get the current face value of the six-sided die."""
        return self.face_value

    def __repr__(self):
        """Return a string representation of the six-sided die."""
        return f'SixSideDie({self.face_value})'

class TenSideDie(SixSideDie):
    """Class representing a ten-sided die, inheriting from the SixSideDie class."""

    def __init__(self):
        """Initialize the ten-sided die."""
        self.sides = 10

    def __repr__(self):
        """Return a string representation of the ten-sided die."""
        return 'TenSideDie({})'.format(super().getFaceValue())

class TwentySideDie(SixSideDie):
    """Class representing a twenty-sided die, inheriting from the SixSideDie class."""

    def __init__(self):
        """Initialize the twenty-sided die."""
        self.sides = 20

    def __repr__(self):
        """Return a string representation of the twenty-sided die."""
        return 'TwentySideDie({})'.format(super().getFaceValue())

class Cup():
    """Class representing a cup containing multiple dice."""

    def __init__(self, sixs, tens, twentys):
        """
        Initialize the cup with a specified number of each type of die.

        Args:
            sixs (int): Number of six-sided dice.
            tens (int): Number of ten-sided dice.
            twentys (int): Number of twenty-sided dice.
        """
        self.sixDie = [SixSideDie() for _ in range(sixs)]
        self.tenDie = [TenSideDie() for _ in range(tens)]
        self.twentyDie = [TwentySideDie() for _ in range(twentys)]
        self.total = 0

    def roll(self):
        """Roll all the dice in the cup and return the total result."""
        self.total = sum(d.roll() for d in self.sixDie) + sum(d.roll() for d in self.tenDie) + sum(d.roll() for d in self.twentyDie)
        return self.total

    def getSum(self):
        """Get the sum of face values of all dice in the cup."""
        return sum(d.getFaceValue() for d in self.sixDie) + sum(d.getFaceValue() for d in self.tenDie) + sum(d.getFaceValue() for d in self.twentyDie)

    def __repr__(self):
        """Return a string representation of the cup."""
        dies = []
        dies.extend(self.sixDie)
        dies.extend(self.tenDie)
        dies.extend(self.twentyDie)
        return ','.join([d.__repr__() for d in dies])

# Example usage
cup = Cup(1, 1, 2)
print(cup.roll())  # Roll the cup
print(cup.getSum())  # Get the sum of face values of all dice in the cup
print(cup)  # Print the cup's contents
