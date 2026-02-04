password = ""

attempts = 0

while password != "secert123":
    password = input("enter a password: ")
    attempts +=1
    
print("Access granted!")
print(f"the number of attempts is:{attempts}")