student = {
    "name": input("Enter student name: "),
    "grades": []
}
total = 0
for x in range(3):
    grade = float(input("enter your grade: "))
    total += grade
    student["grades"].append(grade)  

average = total/len(student["grades"])

student["average"]=average
print(student,f"{student["name"]} average is:{average}")