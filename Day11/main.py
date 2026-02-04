def greet(first, last, greeting="Hello"):
    return f"{greeting},{first},{last}!"
# all in posation
x = greet("shahram","Hatami","Hello")
print(x)

# Mix of positional and keyword
y = greet("shahram","Hatami",greeting = "Hi")
print(y)

# All keyword
z = greet(first = "Shahram",last = "Hatami",greeting = "Hey")
print(z)