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


options = ["easy", "medium", "hard"]

difficulty = string_checker("Difficulty: Easy, Medium or Hard? >>> ", options)
print(difficulty)

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