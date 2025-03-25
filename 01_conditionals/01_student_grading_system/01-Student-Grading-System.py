# Name:        Nehayesh
# Purpose:     To provide a sample program about the basics of Python
# Author:      Mr. Linowski
# Created:     27-feb-2025
# Prompt the user to enter their score
score = int(input("Enter your score (out of 100): "))

#if the score is ("between 90 and 100"): 'print grade A'
if score >= 90:
    print("Grade: A")
    print("you are amazing!!!!")
    print("we are so happy and proud of you🤩")
#if the score is between 80 and 90: 'print grade B'
elif score >= 80:
    print("Grade: B")
    print('you are doing a good job')
#if the score is between 60 and 70: 'print grade c'
elif score >= 70:
    print("Grade: C")
#if the score is less than 60: 'print fail and needs tp redo the course'
elif score >= 60:
    print("Grade: D")
    print("need more practice 😄 ")
else:
    print("Grade: F")
    print("you have to redo the course")
    print('you should ay more attention and be in class on time 🤷‍♀️')
