# example.py
# Python Conditional Statements – Practice Tasks

# Task 1: Single 'if' statement
# Write a program that checks if a number is positive.
# If it is, print "The number is positive."

# Your code here:
number =float( input("Enter a number for cheacking:"))
if number > 0:
    print("The",number,"is possitive")

# Task 2: 'if...else' statement
# Write a program that checks if a number is even or odd.
# Print "Even" if the number is even, otherwise print "Odd".

# Your code here:
number = float(input("Enter a number for cheackinfg:"))
if number == 0 :
    print("The number is zero")
elif number % 2 == 0:
    print("even")
else:
    print("odd")


# Task 3: 'if...elif...else' statement
# Write a program that takes a student's score (0–100) and prints their grade:
# 90–100: "A"
# 80–89: "B"
# 70–79: "C"
# 60–69: "D"
# Below 60: "F"

# Your code here:
number = int(input("Please enter your score:"))
if number >= 90 and number <= 100:
    print("A")
elif number >= 80 and number <= 89:
    print("B")
elif number >= 70 and number <= 79:
    print("C")
elif number >= 60 and number <= 69:
    print("D")
else:
    print("F")


# Task 4: Nested 'if' statement
# Write a program that checks if a number is positive.
# If it is positive, further check if it is even or odd and print the result.
# If it's not positive, just print "Number is not positive."

# Your code here:
number = int(input("Enter a number cheacking:"))
if number > 0:
    if number % 2 == 0:
        print("Even")
    elif number % 2 != 0:
        print("Odd") 
    else:
        print("Zero")
else:
    print("The number is negative")               




# Task 5: Ternary 'if' (conditional expression)
# Use a one-line conditional to assign "Adult" to variable 'status' if age >= 18,
# otherwise assign "Minor". Assume age = 20. Print 'status'.

# Your code here:
age = 20
status = "Adult" if age >= 18 else "Minor"
print("status")



# Task 6: Logical operators (and, or, not)
# Write a program that checks if a person is eligible to vote:
# - Must be at least 18 years old AND
# - Must be a citizen (represented by a boolean variable 'is_citizen')
# Print "Eligible to vote" if both conditions are True, otherwise print "Not eligible".

# Test with: age = 17, is_citizen = True

# Your code here:
age =int(input("Please enter your age:"))
is_citizen = input("are you a citizen?(yes/no) \n ").lower()
if age>= 18 and is_citizen == 'yes':
    print("You are eligible for voting")
else:
    print("You are not eligble for voting")   
