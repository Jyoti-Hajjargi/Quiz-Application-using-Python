# -*- coding: utf-8 -*-
"""1_Quiz Application using Python

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Uhf-kPSRVgoS2bJqXf5fpaUqaQkS0fgE
"""

import random  # Importing the random module to shuffle questions

# List of questions and answers
questions = [
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": ["6", "8", "9", "12"],
        "answer": "8"
    },
    {
        "question": "Which of the following is not a Python data type?",
        "options": ["List", "Tuple", "Stack", "Dictionary"],
        "answer": "Stack"
    },
    {
        "question": "What keyword is used to define a function in Python?",
        "options": ["func", "def", "function", "lambda"],
        "answer": "def"
    },
    {
        "question": "What does the 'len()' function do in Python?",
        "options": ["Returns the number of elements in an iterable", "Returns the type of a variable", "Calculates the sum of elements", "Finds the largest element"],
        "answer": "Returns the number of elements in an iterable"
    },
    {
        "question": "Which of the following is used to handle exceptions in Python?",
        "options": ["try-except", "if-else", "for-while", "do-while"],
        "answer": "try-except"
    },
    {
        "question": "What is the output of print(type([]))?",
        "options": ["<class 'list'>", "<class 'tuple'>", "<class 'dict'>", "<class 'set'>"],
        "answer": "<class 'list'>"
    },
    {
        "question": "Which module in Python is used to generate random numbers?",
        "options": ["os", "sys", "random", "math"],
        "answer": "random"
    },
    {
        "question": "What is the purpose of the 'with' statement in Python?",
        "options": ["To simplify exception handling", "To handle file operations efficiently", "To create loops", "To define functions"],
        "answer": "To handle file operations efficiently"
    },
    {
        "question": "What is the correct way to write a comment in Python?",
        "options": ["# This is a comment", "// This is a comment", "/* This is a comment */", "<!-- This is a comment -->"],
        "answer": "# This is a comment"
    },
    {
        "question": "What is a lambda function in Python?",
        "options": ["A function defined using the 'lambda' keyword", "A function with no name", "A function that can have any number of arguments but only one expression", "All of the above"],
        "answer": "All of the above"
    }
]

# Function to execute the quiz
def quiz():
    score = 0  # Initialize score to zero
    random.shuffle(questions)  # Shuffle the order of questions for randomness

    # Loop through each question
    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")  # Display the question
        for j, option in enumerate(q['options'], 1):  # Display the options
            print(f"{j}. {option}")

        # Take user input and validate it
        try:
            user_answer = int(input("Enter the option number (1-4): "))  # Get user input
            # Check if the answer is correct
            if q['options'][user_answer - 1] == q['answer']:
                print("Correct!")  # Display correct message
                score += 1  # Increment score
            else:
                print(f"Wrong! The correct answer is: {q['answer']}")  # Display correct answer
        except (ValueError, IndexError):  # Handle invalid input
            print("Invalid input. Moving to the next question.")

    # Display final score
    print(f"\nYou scored {score}/{len(questions)}.")

# Main block to start the quiz
if __name__ == "__main__":
    print("Welcome to the Python Interview Quiz Application!")  # Welcome message
    quiz()  # Call the quiz function