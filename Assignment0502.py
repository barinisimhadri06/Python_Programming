# Author: Barini Simhadri
# Date: 13-02-2024
# Honor Statement: "I have not given or received any unauthorized assistance on this assignment."
# link:https://youtu.be/PG1hFmk4hnQ

import random

class Dice:
    """Class representing a single die."""
    def __init__(self, sides):
        """Initialize the dice with the number of sides."""
        self.sides = sides
    
    def roll(self):
        """Simulate rolling the die and return the result."""
        return random.randint(1, self.sides)

class Cup:
    """Class representing a cup containing multiple dice."""
    def __init__(self):
        """Initialize the cup with an empty dictionary to hold dice counts."""
        self.dice_count = {}
    
    def add_dice(self, sides, count):
        """
        Add a specified number of dice with a given number of sides to the cup.
        
        Args:
            sides (int): Number of sides for the dice.
            count (int): Number of dice to add to the cup.
        """
        if sides in self.dice_count:
            self.dice_count[sides] += count
        else:
            self.dice_count[sides] = count
    
    def roll(self):
        """Roll all the dice in the cup and return the total result."""
        total = 0
        for sides, count in self.dice_count.items():
            dice = Dice(sides)
            for _ in range(count):
                total += dice.roll()
        return total

def calculate_score(roll, goal):
    """
    Calculate the score based on the difference between the rolled number and the goal number.
    
    Args:
        roll (int): The number obtained by rolling the dice.
        goal (int): The target number to match or get close to.
        
    Returns:
        int: The score earned based on the roll compared to the goal.
    """
    difference = abs(roll - goal)
    if difference == 0:
        return 10
    elif difference <= 3:
        return 5
    elif difference <= 10:
        return 2
    else:
        return 0

def main():
    """Main function to execute the game."""
    print("Welcome to the Dice Rolling Game!")
    player_name = input("Enter your name: ")
    total_score = 0
    
    while True:
        print("\nLet's start a new game!")
        goal = random.randint(1, 100)
        print(f"\nThe goal number is: {goal}")
        
        cup = Cup()
        for sides in [6, 10, 20]:
            count = int(input(f"How many {sides}-sided dice do you want to roll? "))
            cup.add_dice(sides, count)
        
        roll = cup.roll()
        print(f"\nYou rolled: {roll}")
        
        score = calculate_score(roll, goal)
        total_score += score
        
        print(f"\n{player_name}, your score for this round is: {score}")
        print(f"Your total score is now: {total_score}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print(f"\n{player_name}, thank you for playing! Your final score is: {total_score}")
            break

if __name__ == "__main__":
    main()