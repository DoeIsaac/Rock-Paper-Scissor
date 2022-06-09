#Rock Paper Scissor game

import random

options = ["R", "P", "S"]
user_choice = input("Choose: R - for Rock, P- for Paper, S- for Scissor: ")
computer_choice = random.choice(options)


while user_choice.upper()  not in options:
     print("Error: You enter an invalid option.")
     user_choice = input("Choose: R - for Rock, P- for Paper, S- for Scissor: ")
     user_Choice = user_choice.upper()

if user_choice.upper() == "R" and computer_choice == options[1]:
    print("User: Rock and Computer: Paper")
    print("You loose")
elif user_choice.upper() == "R" and computer_choice == options[2]:
    print("User: Rock and Computer: Scissor")
    print("You Win")
elif user_choice.upper() == "P" and computer_choice == options[0]:
    print("User: Paper and Computer: Rock")
    print("You Win")
elif user_choice.upper() == "P" and computer_choice == options[2]:
    print("User: Paper and Computer: Scissor")
    print("You loose")
elif user_choice.upper() == "S" and computer_choice == options[0]:
    print("User: Scissor and Computer: Rock")
    print("You loose")
elif user_choice.upper() == "S" and computer_choice == options[1]:
    print("User: Scissor and Computer: Paper")
    print("You Win")
elif user_choice.upper() == "R" and computer_choice == options[0]:
    print("User: Rock and Computer: Rock")
    print("Its a draw...")
elif user_choice.upper() == "P" and computer_choice == options[1]:
    print("User: Paper and Computer: Paper")
    print("Its a draw...")
elif user_choice.upper() == "S" and computer_choice == options[2]:
    print("User: Scissor and Computer: Scissor")
    print("Its a draw...")
else:
    print("Error")
