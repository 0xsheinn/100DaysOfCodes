#!/usr/bin/env python
#sheinkhant


student_scores = [43,64,87,98,76,55,34]#input("Input a list of student score: ")
for n in range(0, len(student_scores)):
	student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for score in student_scores:
	if score > highest_score:
		highest_score = score

print(f"The highest score in the class is: {highest_score}")

#can also use max() function

