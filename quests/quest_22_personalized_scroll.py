#!/bin/bash/env python3
def personalized_greeting(name_input, quest_input):
    print (f"Hello {name_input}, your quest is {quest_input}")

#defining name and quest
name_input = input("Please put your name here: ")
quest_input = input("Please put your quest her: ")

personalized_greeting(name_input, quest_input)
