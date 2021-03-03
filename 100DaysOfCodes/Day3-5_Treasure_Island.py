#!/usr/bin/env python3

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure. ")
choice1 = input("You\'re at a crossroad, where do you want to go? Type 'left' or 'right'.").lower()

if choice1 == "left":
	choice2 = input("You\'ve come to a lake. There is an island in the middle of the lake . Type 'wait' to wait a boat. Type 'swim' to swim across.").lower()
	if choice2 == "wait":
		choice3 = input("You arrive at the island unharmed. There is a house with 3 doors, One red, one yellow and one blue. Which color do you choose? ").lower()
		if choice3 == "red":
			print("It is a room full of fire. Game Over!.")
		elif choice3 == "yellow":
			print("You found the treasure! You win!")
		elif choice3 == "blue":
			print("YOu enter a room of beasts. Game Over!")
		else:
			print("You chose a door that doesn't exit. Game Over!.")
	else:
		print("You got attacked by angry trout. Game Over!.")


else:
	print("You fell into a hole. Game Over!.")


