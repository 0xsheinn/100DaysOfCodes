#!/usr/bin/env python3
#sheinkhant
#hangman game
import random
import os
from Day7_Hangman_art_module import logo, stages
from Day7_Hangman_words_module import word_list

end_of_game = False
#TODO-1 - Randomly choose a word from the word list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase
lives = 6
print(logo)
#print(f"chosen word is {chosen_word}")

display = []
for _ in range(word_length):
	display += "_"
print(display)

while not end_of_game: 
	guess = input("Guess a letter: ").lower()
	os.system("clear")
	#check guessed letter
	if guess in display:
		print(f"You've already guessed {guess}.")

	for position in range(word_length):
		letter = chosen_word[position]
		if letter == guess:
			display[position] = letter

	if guess not in chosen_word:
		print(f"You guessed {guess}, that's not in the word. You lose a life.")

		lives -= 1
		if lives == 0:
			end_of_game = True
			print("\nYou lose.\n")

	print(f"{' '.join(display)}")

	if not "_" in display:
		end_of_game = True
		print("\nYou win.\n")

	print(stages[lives])