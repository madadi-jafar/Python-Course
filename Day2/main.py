full_name = input("Enter your full name: ").strip()

# convert name to title case
title_case = full_name.title()

# full name length ignoring the spaces
fulname_without_space = len(full_name.replace(" ",""))

# reversion of full name
reversedOf_full_name = full_name[::-1]

# printing the output
print("Full Name:",title_case)
print("Full name length without space:",fulname_without_space)
print("Reversed of full name:",reversedOf_full_name)