student = {"name":input("Enter your name: "),
           "grade":[]
           }

total = 0

for i in range(1,4):        
    while True:
        try:
            score = float(input(f"please enter number \"{i}\" score: "))
            break
        except ValueError:
            print("Error! not valid")
            continue
    total = total + score
average = total / i

student["grade"].append(average)

print(student)
