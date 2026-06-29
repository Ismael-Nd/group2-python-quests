#!/usr/bin/env python3
def start():
    print("You stand at the mouth of a dark cave. A path also leads into a forest.")
    choice = input("Do you enter the (cave) or the (forest)? ").lower()
    if choice == "cave":
        cave()
    elif choice == "forest":
        forest()
    else:
        print("You hesitate too long and night falls. Game over.")


def cave():
    print("\nInside the cave you find a sleeping dragon guarding a pile of gold.")
    choice = input("Do you (steal) the gold or (leave) quietly? ").lower()
    if choice == "steal":
        print("\nThe dragon wakes and roars! You barely escape with a single coin.")
        print("ENDING: The Lucky Thief.")
    else:
        print("\nYou leave the dragon in peace and find a hidden exit full of gems.")
        print("ENDING: The Wise Wanderer.")


def forest():
    print("\nIn the forest you meet a talking wolf offering a shortcut.")
    choice = input("Do you (trust) the wolf or (refuse)? ").lower()
    if choice == "trust":
        print("\nThe wolf leads you safely to a village. You are hailed as a hero!")
        print("ENDING: The Trusted Hero.")
    else:
        print("\nYou wander alone and get lost as the trees close in around you.")
        print("ENDING: The Lost Soul.")


print("=== The Adventure Begins ===")
start()
