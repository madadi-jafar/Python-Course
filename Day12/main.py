#global variable counter
counter = 0

def increment():
    
    #use the global variable locally
    global counter

    #increment it by 1
    counter += 1

#callfunction variable 3 time
for _ in range(3):
    increment()


print(f"The final valuse of counter is {counter}")
