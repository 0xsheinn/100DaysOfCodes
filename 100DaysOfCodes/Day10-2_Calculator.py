#!/usr/bin/env python3
#sheinkhant
import os

logo =''' 
	 .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. |
| |     ______   | || |      __      | || |   _____      | || |     ______   | |
| |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------' 

'''


def add(n1, n2):
	return n1 + n2

def subtract(n1, n2):
	return n1 - n2

def multiply(n1, n2):
	return n1 * n2

def divide(n1, n2):
	return n1 / n2

operations = {
	"+": add,
	"-": subtract,
	"*": multiply,
	"/": divide
}

def calculation():
	os.system("clear")
	print(logo)
	num1 = float(input("Whatis the first number? : "))

	for symbol in operations:
		print(symbol)

	should_continue = True

	while should_continue:
		operation_symbol = input("Pick an operation: ")
		num2 = float(input("Whatis the next number? : "))

		calculation_function = operations[operation_symbol]
		answer = calculation_function(num1, num2)

		print(f"{num1} {operation_symbol} {num2} = {answer}")

		if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start new calculation.: ") == 'y':
			num1 = answer
		else:
			should_continue = False
			calculation()

calculation()


