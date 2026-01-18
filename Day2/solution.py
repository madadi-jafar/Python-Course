# Day 2: String Manipulation & Type Conversion:

# Starter code:
full_name = input("Enter your full name: ").strip()
title_case_name = full_name.title()
# Print the title case name
print("Title Case Name:", title_case_name)

letters_count = len(full_name.replace(" ", ""))
print("Letters Count:", letters_count)

reversed_name = full_name[::-1]
print("Reversed Name:", reversed_name)
