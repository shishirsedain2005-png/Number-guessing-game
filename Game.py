    # number guessing game
import random
print("Hey, I am thinking number between 1 and 20.")
computer_guess=random.randint(1,20)
count=0
while count<5:
        try:
            user_guess=int(input("Enter your number->"))
        except ValueError:
            print("please input valid number")
            continue
        count+=1
        if user_guess==computer_guess:
            print (f'Your guess is correct. Its{user_guess} and you guessed it in {count} times')
            break
        else:
            if user_guess>computer_guess:
                print("Too High!!")
            elif user_guess<computer_guess:
                print("Too Loww!!")

else:
        print("Game Over!!")
        print(f'The correct number was{computer_guess}')

            


