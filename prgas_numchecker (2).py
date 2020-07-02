import random

def int_check(question):
    valid = False
    while not valid:
        try:
            response = int(input(question))
            valid = True
            return response

        except ValueError:
            print("You did not enter an INTEGER. Please try again")

def num_check(question, low, high):

    error = "Please enter a number between {} and {}".format(low, high)

    valid = False
    while not valid:
        try:
            response = int(input(question))
            if low - 1 < response < high + 1:
                return response
            else:
                print(error)

        except ValueError:
            print("You did not enter an INTEGER. Please try again")

# colour list

red = "\u001b[31m"

green = "\u001b[32m"

gold = "\u001b[33m"

dblue = "\u001b[34m"

pink = "\u001b[35m"

lblue = "\u001b[36m"

grey = "\u001b[37m"

colour_end = "\u001b[0m"

# min_num = -100
# max_num = 100
#
# a = random.randrange(0, max_num)
# b = random.randrange(min_num, max_num)

# if a > b:
#     sign = "-"
# else:
#     sign = "+"
# print(a)
# print(b)
#
# if b < 0:
#     b = b * (-1)
#     print(b)
#     sign = "- "
# else:
#     sign = "+ "
#
#
# answer = a + b*(-1)
#
# print(answer)
# question = int(input("what's {} {}{}? ".format(a, sign, b)))
# if question == answer:
#     print("good")
#
# else:
#     print("bad")


range_num = num_check("Enter a maximum value (minimum is one) >>> ", 1, 10)
high_num = num_check("Enter a maximum value for your number range >>> ", range_num + 1, 1000)

keep_going = ""
while keep_going == "":
    a = random.randrange(1, range_num)
    b = random.randrange(range_num + 1, high_num)

    # answer_more = a + b
    # print(answer_more)
    question_more = int(input("What is {} more than {}? ".format(a, b)))
    options = "A - {}\nB - {}\nC - {}\nD - {}".format(a + b, a - b, random.randrange(a, b), a * 3 + b)
    print(options)

    # answer_less = b - a
    # print(answer_less)
    question_less = int(input("What is {} less than {}? ".format(a, b)))

    keep_going = input("\nPress <enter> to play again or any key to quit: \n")
