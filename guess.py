import random

def main():
    goal = random.randint(0, 500)
    guess = 0
    i = 0
    print('I\'m thinking of a number.', end= ' ')
    
    while guess != goal:
        guess = input("Take a guess: ")
        if guess.isnumeric():
            guess = int(guess)
            if 0 <= guess <= 500: 
                if guess < goal:
                    print("Too low!")
                elif guess > goal:
                    print('Too high!')
            else:
                print('Hint: the answer is between 0 and 500')
        else:
            print('Hint: the answer is a positive number.')
        i += 1
    print(F'Success! It took you {i} tries.')
    
main()  
    
    
    
'''    
    if not guess.isnumeric() and 0 <= guess < 501:
        print("Hint: the goal is a positive number between 0 and 500")
        
    while guess != goal:
        
        guess = input("Take a guess: ")
        if guess.isnumeric() and 0 <= guess < 501:
            print("Try again!")
        else:
            print("Hint: the goal is a positive number between 0 and 500")
'''

    