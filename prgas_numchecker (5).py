import random

print("✔ or ❌")


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

def outcomes(user, computer):
    player_wins = 0
    computer_wins = 0

    if user == computer:
        result = ""


game_difficulty = ["easy", "medium", "hard"]

questions = ["A", "B", "C"]

# if difficulty == "easy":
#     min_num = 1
#     max_num = 100
#
# elif difficulty == "medium":
#     min_num = round(-50), 1
#     max_num = round(50), 1
#
# else:
#     min_num = round(-50), 2
#     max_num = round(50), 2

difficulty = string_checker("Easy, Medium or Hard? >>> ", game_difficulty)

if difficulty == "easy":
    min_num = 1
    max_num = 100

elif difficulty == "medium":
    min_num = round(-50), 1
    max_num = round(50), 1

else:
    min_num = round(-50), 2
    max_num = round(50), 2


print(min_num)
print(max_num)

user = string_checker("What's {} more than {}? >>> ",  questions)
