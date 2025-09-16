# Task create a dice game
# Import integers as dice
import random
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

# count the the total number
total = die1 + die2

# check the condition
if total == 7 or total == 11:
    print(f"you win the game! the result is {total}.")
elif total == 2 or total == 3 or total == 12:
    print(f"you lose the game! the result is {total}")
else:
    print(f"Roll again! it was daw. the result is {total}")