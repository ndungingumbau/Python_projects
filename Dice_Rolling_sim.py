# import random
# define a function to roll the dice
# create a dictionary that will have the drawings of the dice

import random

def roll_dice():

    roll = input("Roll dice? (Yes/No): ")

    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("dice rolled: {} and {}".format(dice1, dice2))

        roll = input("Roll again? (Yes/No): ")

roll_dice()        