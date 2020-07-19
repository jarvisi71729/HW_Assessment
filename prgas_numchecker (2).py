import random
from random import randint

# def int_check(question):
#     valid = False
#     while not valid:
#         try:
#             response = int(input(question))
#             valid = True
#             return response
#
#         except ValueError:
#             print("You did not enter an INTEGER. Please try again")


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


def string_checker(question, to_check):
    valid = False
    while not valid:

        response = input(question).lower()

        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item

        print("Sorry that is not a valid response")


# colour list

red = "\u001b[31m"

green = "\u001b[32m"

gold = "\u001b[33m"

dblue = "\u001b[34m"

pink = "\u001b[35m"

lblue = "\u001b[36m"

grey = "\u001b[37m"

colour_end = "\u001b[0m"

options = ["easy", "medium", "hard"]


# difficulty = string_checker("Difficulty: Easy, Medium or Hard? >>> ", options)

# rounds = num_check("How many rounds would you like to play? ", 1, 10)

# if difficulty == "easy":
#     min_num = 1
#     max_num = 100
#
# elif difficulty == "medium":
#     # min_num = round(random.uniform(-100, 0), 1)
#     # max_num = round(random.uniform(0, 100), 1)
#     min_num = -100.0
#     max_num = 100.0
#
# else:
#     # min_num = round(random.uniform(-50), 2)
#     # max_num = round(random.uniform(50), 2)
#     min_num = -100.00
#     max_num = 100.00

player = False

keep_going = ""
while keep_going == "":
    # a = random.randrange(1, range_num)
    # b = random.randrange(range_num, high_num)

    # answer_more = a + b
    # print(answer_more)

    rounds = num_check("How many rounds would you like to play? ", 1, 10)

    correct_counter = 0
    wrong_counter = 0

    while rounds > correct_counter and rounds > wrong_counter:

        while player is False:

            min = -100
            max = 100

            # test = ["a", "b", "c", "d"]
            # answers = "A - {}\nB - {}\nC - {}\nD - {}".format(a + b, a - b, random.randrange(a, b), a * 3 + b)

            # tf = "• A - True\n• B - False"
            # check = ["a", "b", "c"]

            # t = ["True", "False", "Unsolvable"]
            #
            # ran = t[randint(0, 2)]

            to_check_abc = "• A - Greater\n• B - Lesser\n• C - They are equal"
            to_check_tf = "• A - True\n• B - False"

            check = ["a", "b", "c"]

            # print("Difficulty chosen: {}"
            #       "\nThe number range for difficulty {} is:"
            #       "\nMinimum: {}"
            #       "\nMaximum: {}"
            #       .format(difficulty, difficulty, min_num, max_num))

            easy = string_checker("Is {} greater or less than {}? \n{} \n>>> ".format(random.randrange(min, 0),
                                                                                      random.randrange(0, max),
                                                                                      to_check_abc), check)
            hard = string_checker("Is {} equal to {}? \n{} \n>>> ".format(random.randrange(min, 0), random.randrange
                                                                            (0, max), to_check_tf), check)

            google = ["easy", "hard"]

            question = google[randint(0, 1)]

            print(question)

            # question_more = string_checker("Is {} greater than {}? \n{} \n>>> ".format(a, b, to_check_abc), check)

            if min > min:
                if easy == "a":
                    print("Correct")
                    correct_counter += 1

                else:
                    print("Incorrect")
                    wrong_counter += 1

            elif max > min:
                if easy == "b":
                    print("Correct")
                    correct_counter += 1

                else:
                    print("Incorrect")
                    wrong_counter += 1
            else:
                if max == min:
                    if easy == "c":
                        print("Correct")
                        correct_counter += 1

                    else:
                        print("Incorrect")
                        wrong_counter += 1

            # options = "A - {}\nB - {}\nC - {}\nD - {}".format(a + b, a - b, random.randrange(a, b), a * 3 + b)
            # print(options)

            # answer_less = b - a
            # print(answer_less)
            # question_less = int(input("What is {} less than {}? ".format(a, b)))

            keep_going = input("\nPress <enter> to play again or any key to quit: \n")
