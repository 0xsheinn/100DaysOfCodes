#!/usr/bin/env python3
#sheinkhant
import random
import os

logo = """
  _ _ _ _ ___ ___ _ _ _ ___ _ _ _________
 |A|Q|1|5|4  |7  |J|1|9|7  |A|K|2        |
 |@|@|@|@|@  |## |O|O|O|OO |+|+|+        |
 | | | | | @ |   | | | |   | | |    +    |
 | | | | |   | # | | | | O | | |         |
 | | | | | @ |   | | | |   | | |    +    |
 | | | | |   | # | | | | O | | |        +|
 | | | | |   |   | | | |   | | |        Z|
  ~ ~ ~ ~ ~~~ ~~~ ~ ~ ~ ~~~ ~ ~ ~~~~~~~~~
	
"""

def deal_card():
	'''Returns a random card from the deck.'''
	cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
	card = random.choice(cards)
	return card 

def calculate_score(cards):
	if sum(cards) == 21 and len(cards) == 2:
		return 0

	if 11 in cards and sum(cards) > 21:
		cards.remove(11)
		cards.append(1)

	return sum(cards)

def compare(user_score, computer_score):

	if user_score == computer_score:
		return "\nDraw!\n"
	elif computer_score == 0:
		return "\nLose, opponent has Blackjack :(\n"
	elif user_score == 0:
		return "\nWin with a Blackjack :)\n"
	elif user_score > 21:
		return "\nYou went over. You lose :(\n"
	elif computer_score > 21:
		return "\nOpponent went over. You win! :)\n"
	elif user_score > computer_score:
		return "\nYou win! :)\n"
	else:
		return "\nYou Lose! :(\n"


def play_game():
	print(logo)

	user_cards = []
	computer_cards = []
	is_gameover = False

	for _ in range(2):
		user_cards.append(deal_card())
		computer_cards.append(deal_card())


	while not is_gameover:
		user_score = calculate_score(user_cards)
		computer_score = calculate_score(computer_cards)

		print(f"Your cards: {user_cards}, current score is {user_score}")
		print(f"Computer's first cards: {computer_cards[0]}")

		if user_score == 0 or computer_score == 0 or user_score > 21:
			is_gameover = True
		else:
			user_should_deal = input("\nType 'y' to get another card, type 'n' to pass: ")
			if user_should_deal == "y":
				user_cards.append(deal_card())
			else:
				is_gameover = True

	while computer_score != 0 and computer_score < 17:
		computer_cards.append(deal_card())
		computer_score = calculate_score(computer_cards)

	print(f"\nYour final hand: {user_cards}, final score: {user_score}")
	print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
	print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
	os.system("clear")
	play_game()


