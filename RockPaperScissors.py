import random

# function get_choices


def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

# functions can receive data, data is called arguments
# "" <- are optional for return


def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You lose."
        else:
            return "Scissors cuts paper! You lose."
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose."


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)

# refactoring is process of restructuring code


# example of if else statement:
# age = 20
# if age >= 18:
#       print("You are an adult.")
# else:
#       print("You are a child.")

# elif just stands for else if combines else and if
# if age >= 18:
#     print("You are an adult.")
# elif age > 12:
#     print("You are a teenager.")
# elif age > 1:
#     print("You are a child.")
# else:
#     print("You are a baby.")


# f-strings allow you to make strings with variables
# and other python code
# ex:
# age = 25
# print(f"Jim is {age} years old.")


# ex:
# a = 3
# b = 5
# if a != b:
#   print("yes")

# variable choices = function get_choices
# choices = get_choices()
# print(choices)

# dictionaries in python are used to store data values in key value pairs

# example:
# dict = {"name": "beau", "color": "blue"}
# the value in a dictionary can be variable so instead of blue
# it can be choices

# A list in python is used to store multiple items in a
# single variable. Lists are surrounded by brackets and each
# each item is separated by a ,
# ex: food = ["pizza", "carrots", "eggs"] <-- list of strings
# dinner = random.choice(food) <- using random library
