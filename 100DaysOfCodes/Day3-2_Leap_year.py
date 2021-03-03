#!/usr/bin/env python3
#author:sheinkhant
year = int(input("Which year do you wnat to check?"))

if year % 4 == 0:
	if year % 100 != 0:
		if year % 400 == 0:
			print(f"{year} is leap year.")
		else:
			print(f"{year} is not leap year.")
	else:
		print(f"{year} is a leap year.")
else:
	print(f"{year} is not leap year.")