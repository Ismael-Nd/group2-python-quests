#LEVEL 3
#Quest 11: The Guardian of the Bridge
#Concept: if statement - This lets your program make a decision.
#How to use it: if age > 18: print("You may pass.")
#Why it's important: This is how programs become "smart." They can react differently to different situations.
#Logical Reasoning: If a specific condition is met, then execute the following code.
#The Quest: Ask for the user's age. If it's 18 or greater, print a message that they are old enough to vote.
age = int(input("Please enter your age: "))

if age >= 18:
    print("You are old enough to vote")
else: 
    print("You have a few years to go")