# Author: Brandon Jacks
# Section: CIS 225 01
# Date: 10/5/22
# File: Letter_Grade.py
#
# A Program that tells you a letter grade based off an entered numeric grade

def main():
    letter_grade = input("Enter your numeric grade: ")
    
    valid = letter_grade.isnumeric()
    if valid == True:
        letter_grade = int(letter_grade)
        if 89 < letter_grade < 101:
            print("Your grade is: A")
        elif 79 < letter_grade < 90:
            print("Your grade is: B")
        elif 69 < letter_grade < 80:
            print("Your grade is: C")
        elif 59 < letter_grade < 70:
            print("Your grade is: D")
        elif letter_grade < 60:
            print("Your grade is: F")
    else:
        print("You must enter a number.")
main()