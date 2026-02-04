# create the function ie_even
def is_even(n):

    # return true n is even
    return n % 2==0
    

def print_parrity(x):
    
    # use the function is_even to check the condition
    if is_even(x):
        print("Even")

    else:
        print("Odd")

# Handle the possible error
while True:

    try:
        number = int(input("Enter an integer: "))
        
        if number % 2 == 0:
            print(f"Does the entered  number is even? {is_even(number)}")
            print_parrity(number)
        else:
            print(f"does the number is even? {is_even(number)}")
            print_parrity(number)
        break
    
    except ValueError:
        print("Please enter an integer:")
        continue