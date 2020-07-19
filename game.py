import time
import random

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


def num_check(question, low, high):
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                valid = True
                return response
            else:
                print("You did not enter a number between {} and {}".format(low, high))
        except ValueError:
            print("Invalid input")


print("Welcome to the True or False Game!")
time.sleep(1)
rounds = num_check("How many rounds would you like to play? ", 3, 10)
counter = 0
while counter <= rounds - 1:
    if rounds in range(3, 10):
        time.sleep(1)
        print("Challenge accepted! I will play you for", rounds,"rounds!")

    check = ["t", "f"]
    a = random.randrange(-100, 100)
    b = random.randrange(-100, 100)
    user = string_checker("Is {} greater than {}? >>> ".format(a, b), check)
    answer = ""

    if user == "t":
        if a > b:
            print("Correct")
            counter += 1

        else:
            print("Wrong")
            counter += 1

    if user == "f":
        if b > a:
            print("Correct")
            counter += 1

        else:
            print("Wrong")
            counter += 1

    if user == rounds:
        print("Thank you for playing the True or False Game!")