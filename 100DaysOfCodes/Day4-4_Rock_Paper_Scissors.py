#!/usr/bin/env python3
#sheinkhant
import random

rock = ''' ascii here '''
paper = ''' ascii here '''
scissors = ''' ascii here '''

games_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
print(games_images[user_choice])

computer_choice = random.randint(0,2)
print(f"Computer chose: ")
print(games_images[computer_choice])

if user_choice >= 3 or user_choice < 0 :
	print("You typed an invalid number, you lose!.")
elif user_choice == 0 and computer_choice == 2:
	print("You wins!")
elif computer_choice == 0 and user_choice == 2:
	print("You lose!")
elif computer_choice > user_choice:
	print("You lose!")
elif user_choice > computer_choice:
	print("You wins!")
elif computer_choice == user_choice:
	print("It's a draw.")

