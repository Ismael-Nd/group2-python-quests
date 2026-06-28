#Quest 25: The Number Wizard
#The Quest: Upgrade your number guessing game. After each wrong guess, tell the user if their guess was "too high" or "too low".
print("Welcome to the Number Guessing Game")
guess = 0
winning_num = 10
while guess != winning_num:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("You need to enter a number")
        continue
    
    if guess > winning_num:
        print("Too high, try a smaller number")
    elif guess < winning_num:
        print("Too low, try a bigger number")

print(f"Congrats! You have the guessed it. The number is {winning_num}")