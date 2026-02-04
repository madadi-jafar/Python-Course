# ask the user for password 
password =input("Please enter the password: ")

# create variable attemps to count the number of your tries
attemps = 0

# check if password is incorrect; continue
while password != 'secret123':

    password = input("Does not match, please enter again: ")
    
    # increment attemps by one after each iteration
    attemps = attemps + 1

# print the output
print(f"Good job! Access granted! you password match in \" {attemps +1}\" attemp(s)")

    