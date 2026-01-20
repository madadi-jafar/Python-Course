num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter Operator: (+,-,*,/):")
if op == '+':
    print(round(num1+num2,2))
elif op == '-':
    print(round(num1-num2,2))
elif op == '*':
    print(round(num1*num2,2))
elif op == '/' and num2 == 0:
    print("Error! can not divided by zero")
elif op == '/':
    print(round(num1/num2,2))
else:
    print("Invalid input")