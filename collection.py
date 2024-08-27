import sys
from adventurer import tim
from foodFactory import *


#this will be the environment the player character adds items to their inventory
def store():

    while True:
        print("Welcome to the shop, is there anything you want?\n")
        print("Press 1 for Corn\n")
        print("Press 2 for Apple\n")
        print("Press 3 for Chicken\n")
        print("Press")
        print("Press q to stop\n")

        choice = input()
        if not inputCheck(choice):
            print("invalid input. please try again")
            continue
        
        if choice == 'q':
            tim.display_inventory()
            sys.exit()
        
        addItems(choice)

        


def inputCheck(choice):
    return choice in ['1','2','3','4','q']

def addItems(choice):
    if choice == '1':
        tim.add_food(corn)
    elif choice == '2':
        tim.add_food(apple)
    elif choice == '3':
        tim.add_food(snake)
    elif choice == '4':
        tim.add_food(chicken)
