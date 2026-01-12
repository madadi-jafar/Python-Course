# Task: Ask the user for two numbers and an operator (+, -, *, /).

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

# Check the operator and compute the correct result(rounded)
if op == '+':
    print("The addition of",num1,"+",num2,"=",round(num1+num2,2))
elif op == '-':
    print("The subtraction of",num1,"-",num2,"=",round(num1-num2,2))
elif op == '*':
    print("The multiplication of",num1,"x",num2,"=",round(num1*num2))
elif op == '/' and num2 ==0:
    print("Error can not divide by zero!")
else:
    print("the division of",num1,"/",num2,"=",round(num1/num2,2))