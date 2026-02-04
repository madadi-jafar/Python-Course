def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
number = int(input("Enter an integer: "))
boolean = is_even(number) 
print(boolean)            


def print_parity(x):
    if is_even(x):
        print("Even")
    else:
        print("Odd")
print_parity (number)                