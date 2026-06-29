#!/bin/bash/env python3
a = input("Please tell us if you're going left or right here: ")
if a == "left":
  action = input("Do you swim or wait?")
  if action == "swim":
    print("You will find a hidden treasure.")
  else:
    print("You waited too long. The treasure is gone.")
else:
  print("Game over")
