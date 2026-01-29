import random
die1 = random.randint(1, 6)
print(die1)
die2 = random.randint(1, 6)
print(die2)
total = die1 + die2
if total == 7 or total == 11:
    print("you win")
elif total == 2 or total == 3 or total == 12 :
    print("you lose")
else:
    print("Roll again!")     