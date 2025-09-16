# create an empty list to store the integers' later
num =[]

# create a variable to store the sum of numbers
total = 0
# Get the numbers form the user
for n in range(1,6):

   # take care of possible errors
   while True:
    try:
        number = int(input(f"please enter number \"{n}\": "))
    
        # add numbers in the list
        num.append(number)

        # sum the numbers
        total = total + number
        break

    except ValueError:
       print("Error! required integer: ")
       continue
# get the average of numbers rounded in 2 decimal point
average_of_number = round(total / len(num),2)

# get the largest of the numbers
biggest_of_numbers = max(num) 

# print the result
print()
print(f"your numbers' list is {num}")

print(f"The sum of the numbers is {total}.")

print(f"The average of numbers is {average_of_number}")

print(f"The maximum of numbers is {biggest_of_numbers}")


