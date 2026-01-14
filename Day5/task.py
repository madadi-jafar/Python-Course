# Day 5: Randomisation & Simple Games

import random

# Task: Simulate a dice game.
# Roll two 6-sided dice. If sum is 7 or 11, user wins. If sum is 2, 3, or 12, user loses.
# Otherwise, print "Roll again!".
# Use random.randint(1, 6) for each die.

# Starter code:
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total = die1 + die2
# TODO: Check win/lose/continue conditions and print result