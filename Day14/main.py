quiz = [
    {"question": "What is 2+2?", "options": ["3", "4", "5", "6"], "answer": 1},
    {"question": "Capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": 2},
    {"question": "Python is named after?", "options": ["Snake", "Monty Python", "Pyramid", "Pioneer"], "answer": 1}
]
score = 0
for q in quiz :
    print(f"{q["question"]}")
    for i ,option in enumerate(q["options"]):
        print(f"{i}:{option}")
    while True:
        try:
            user_answer = int(input("Enter the number of answer (0-3): "))
            if 0<= user_answer <= 3:
                break

            else:
                print("Invalid input. enter(0-3)")
        except ValueError:
            print("Invalid input. entre a number.")


    if user_answer == q["answer"]:
        print("crrect!")
        score += 1
    else:
        print("incorrect input.")

print(f"your final score is : {score} out of {len(quiz)}")