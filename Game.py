# number guessing game
import random

while True:
    print("Hey, I am thinking number between 1 and 20.")
    computer_guess=random.randint(1,20)
    print(computer_guess)

    user_guess=int(input("Enter your number->"))

    if user_guess==computer_guess:
        print("Your guess is correct. It's",user_guess)
        break
    else:
        if user_guess>computer_guess:
            print("Too High!!")
        elif user_guess<computer_guess:
            print("Too Loww!!")
        


