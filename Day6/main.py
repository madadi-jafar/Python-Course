import math
# put the loop continuation condition initially true
while True:  
    try:
        number = float(input("Enter a float number"))
        if number < 0 :
            print("please enter a positive float number")
            continue
        break
    except ValueError:
        print("Please enter a float number! ")
        
result = math.sqrt(number)
print(f"the result is {result}")
    
