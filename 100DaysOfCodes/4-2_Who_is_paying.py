#!/usr/bin/env python
#sheinkhant
import random

test_seed = int(input("Create a seed number: "))
ramdom.seed(test_seed)

nameAsCSV = input("Give ma everybody's names,seperated by a comma. ")
names = namesAsCSV.split(", ")

num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today.")
