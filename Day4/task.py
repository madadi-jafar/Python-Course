# Day 4: Logical Operators & Nested Conditionals

# Task: A movie theater charges:
# - $10 if age < 12 or age > 65
# - $15 if 12 <= age <= 65
# But if the user has a "VIP" pass (yes/no), they get 20% off.
# Ask for age and VIP status, then print the final price.

# Starter code:
age = int(input("Enter your age: "))
vip = input("Do you have a VIP pass? (yes/no): ").lower()
# TODO: Determine base price
# TODO: Apply discount if VIP
# TODO: Print final price