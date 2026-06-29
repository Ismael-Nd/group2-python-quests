#!/usr/bin/env python3
age = int(input("How old are you? "))
gold = int(input("How many gold coins do you have? "))

if age >= 18 and gold >= 20:
    print("Welcome in! Enjoy the club.")
else:
    print("Sorry, you cannot enter. You need to be 18+ AND have 20+ gold coins.")
