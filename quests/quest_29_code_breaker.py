#!/usr/bin/env python3

secret_code = 42

for attempt in range(3):
    guess = int(input("Please put your guess here: "))
    
    if guess == secret_code:
        print("You guessed it, Congratulations!!")
        break
    else:
        if attempt < 2:
            print("Try Again")
        else:
            print("Game over! You ran out of attempts.")

