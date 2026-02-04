# Day 14: Final Project – Mini Quiz App

# Task: Create a 3-question quiz using a list of dictionaries.
# Each question dict has: "question", "options" (list), "answer" (index).
# Ask each question, validate input (must be 0,1,2,3), and track score.
# At the end, print total score out of 3.

# Starter code:
quiz = [
    {"question": "What is 2+2?", "options": ["3", "4", "5", "6"], "answer": 1},
    {"question": "Capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": 2},
    {"question": "Python is named after?", "options": ["Snake", "Monty Python", "Pyramid", "Pioneer"], "answer": 1}
]

score = 0
# TODO: Loop through quiz, display questions & options
# TODO: Get user input, validate (0-3), compare to answer
# TODO: Update score
# TODO: Print final score