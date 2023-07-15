 #Guess the number(User have to guess the correct number)

import random   # importing random package from the module to generate random numbers

def guess(x):
    random_number = random.randint(1,x)
    guess = 0

#condition checking
    while guess != random_number:
        guess = int(input(f" Guess a number between 1 and {x} : "))
        if guess < random_number:
            print(" Sorry , guess again and it is too low.")
        elif guess > random_number:
            print(" Sorry , guess again and it is too high.") 

    print(f" Superb , you guessed the  number {random_number} correctly!!!") 

guess(100)   #calling function
