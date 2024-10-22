# a dictionary that stores questions and answers
# have a variable that tracks the score of the player
# loop through using the key value pairs
# display each question to the user and allow them to answer
# show final result when quiz is completed

quiz = {
    "question1": {
        "Question": "what is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
       "Question": "what is the capital of Germany?",
        "answer": "Berlin"
    },
    "question3": {
       "Question": "what is the capital of italy?",
        "answer": "Rome"
    },
    "question4": {
       "Question": "what is the capital of Tanzania?",
        "answer": "Dodoma"
    },
    "question5": {
       "Question": "what is the capital of Austria?",
        "answer": "Vienna"
    },
    "question6": {
       "Question": "what is the capital of Portugal?",
        "answer": "Lisbon"
    },
    "question7": {
       "Question":  "what is the capital of Kenya?",
        "answer": "Nairobi"
    },
}
score = 0

for key, value in quiz.items():
    print(value['Question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score + 1
        print("Your score is: " + str(score))
        print("")
        print("")

    else:
        print("Wrong!")
        print("The answer is : " + value['answer'])
        print("Your score is: " + str(score))
        print("")
        print("")

print("You got " + str(score) + "out of 7 questions correctly")
print("Your percentage is " + str(int(score/7 * 100)) + "%")