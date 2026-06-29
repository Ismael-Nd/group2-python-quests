#!/usr/bin/env python3
guess = 0
winning_num = 10
while guess != winning_num:
    guess = int(input("Enter your guess: "))
print(f"Congrats! You have the guessed it. The number is {winning_num}")