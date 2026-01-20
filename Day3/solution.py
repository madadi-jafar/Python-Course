# Day 3: Mathematical Operations & Conditionals

# Starter code:
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")
# TODO: Use if/elif/else to handle operation
# TODO: Handle division by zero
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = num1 / num2
else:
    print("Invalid operator.")
if op in ["+", "-", "*", "/"] and op != "/":
    print(f"Result: {result:.2f}")
elif op == "/":
    if num2 != 0:
        print(f"Result: {result:.2f}")