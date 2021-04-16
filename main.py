# The idea is to have a repeatable 75 question test. The questions will be customizable beforehand with a maximum number
# used and the type of problems presented (addition, subtraction, etc). After answering a question, you will be told
# if you got it right and what the correct answer is if you did not. At the end, you'll get a score and a time.
import random
import time


def initialize():
    while True:
        print("This is a practice Math Test.")
        print("There will be 75 questions and you will receive a score and a time at the end.")
        max_num = (input("What is the highest integer you would like to appear on the test?"))
        try:  # Make sure that the input is an integer, otherwise return wrong answer
            int_num = int(max_num)
            break
        except ValueError:
            print("That is not an integer.")
    return int_num
    # This part will require input parsing
    # test_type = input("What type of test would you like to take? Please input one of the following: + - * /")


def test_questions(max_num):
    right = 0
    wrong = 0
    start = time.perf_counter()
    for z in range(3):
        x = random.randint(0, max_num)
        y = random.randint(0, max_num)
        reply = input(f"{str(x)} + {str(y)} = ")
        reply = reply.strip()
        answer = x+y
        if reply == str(answer):
            print("Correct!")
            right += 1
        else:
            print(f"Wrong. The answer is {str(answer)}")
            wrong += 1
    stop = time.perf_counter()
    print(f"You got {right} question(s) right and {wrong} question(s) wrong.")
    print(f"Your score is {right / 3 * 100}%.")
    print(f"Your time is {stop - start:0.2f} seconds.")
    return()


biggest_num = initialize()
test_questions(biggest_num)
