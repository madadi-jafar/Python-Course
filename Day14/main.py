# create the quiz list
quiz = [
    {"question": "What is 2+2?", "options": ["3", "4", "5", "6"], "answer": 1},
    {"question": "Capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": 2},
    {"question": "Python is named after?", "options": ["Snake", "Monty Python", "Pyramid", "Pioneer"], "answer": 1}
]

# use variable score to compute user score
score = 0

# display question and options to the user
for key in quiz:

    #check that answers must not be displayed
    if key =="answer":
        continue
    
    # continue to display if everthing is ture
    while True:
        if key != "answer":
            print(key["question"],key["options"])

        # handle the possible error(lack of integer)
        try:
            user_answer = int(input("Valid answers: 0, 1, 2, 3 \n"))
            if user_answer >=0 and user_answer <= 3:
                
                # update the score if true
                if user_answer == key["answer"]: 
                    score +=1
                break
            else:
                print("your answer is not in the options! try again: ")
                continue
        except ValueError:
            print("your answer is not in the options! try again: ")
            continue

print()
for i in quiz:
    print(f"{i}\n")

print(f"your final score is {score} out of {len(quiz)}")
