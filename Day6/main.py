import math
while True:
    try:
        number = float(input("Enter a float number:"))
        print("it is square root is: ",math.sqrt(number))
        break
    except ValueError:
        print("Error!")
        continue
