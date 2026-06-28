#Quest 18: The Loop of Riddles
#Concept: Using a while loop with a user-input condition.
#Why it's important: It's the basis for games, user menus, and data processing.
#Logical Reasoning: I will keep repeating this action until the user provides the correct input to stop the loop.
#The Quest: Write a guessing game. Think of a secret number. Use a while loop to keep asking the user to guess until they get it right.
guess = 0
winning_num = 10
while guess != winning_num:
    guess = int(input("Enter your guess: "))
print(f"Congrats! You have the guessed it. The number is {winning_num}")