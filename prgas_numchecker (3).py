import random


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


def int_check(question):
    valid = False
    while not valid:
        try:
            response = int(input(question))
            valid = True
            return response

        except ValueError:
            print("You did not enter an INTEGER. Please try again")


# items = ["coconuts", "beans", "bananas", "melons", "mice", "balls"]
# names = ["Yaroslav", "Malahomebuttonnowork", "Josha", "Iszac"]
# range_num = num_check("Enter a maximum value (minimum is one) >>> ", 1, 10)
# high_num = num_check("Enter a maximum value for your number range >>> ", range_num + 1, 1000)
#
# user = input("What's your name? >> ")

# question = "if you have {} {} and {} takes {} away, how many do you have left? ")


difficulty = input("Which difficulty would you like to play out of the three options: Easy (E), Medium (M), Hard (H) >>> ")

num_range = difficulty

if difficulty == "Easy" or "E":
    min_num = 1
    max_num = 100

elif difficulty == "Medium" or "M":
    min_num = 1
    max_num = 100

else:
    min_num = 1
    max_num = 100
