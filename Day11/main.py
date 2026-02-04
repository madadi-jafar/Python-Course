def greet(first, last, greeting= "Hello"):
    return f"""
    {[greeting]},{[first],[last]}!
    """

name = input("enter your name: ")
last_name = input("Enter your last name: ")

def all_positional():
    print(greet(name,last_name,"Hello"))

all_positional()

def mix():
    print(greet(name,last = last_name, greeting = "Hello"))

mix()

def all_key():
    print(greet(first = name, last = last_name, greeting = "Hello"))

all_key()