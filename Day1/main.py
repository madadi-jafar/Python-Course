# Task: Ask the user for their name, age, and favorite number.

# Ask th euser for their name
name = input("Enter your name: ")

#Get age and favorite number
age=int(input("Enter your age:"))
favoriteNumber=int(input("Enter your favorite number:"))

# Calculate square of favorite number
favoriteNumberSquare=favoriteNumber ** 2

# print the result
print("Hello, "+name+" you are",age,"years old, and your favorite number squared is",favoriteNumberSquare)