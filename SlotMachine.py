print("Welcome to the Slot Machine!")
numberOfTimes = input('How many times do you want to play?')
slotsPossible = ["bar","bar","bar","cherry","crown","crown"]
from random import *
def play():
    slot1=choice(slotsPossible)
    slot2=choice(slotsPossible)
    slot3=choice(slotsPossible)
    win = ""
    if (slot1==slot2==slot3=="cherry"):
        win = "You win $100"
    if (slot1==slot2==slot3=="crown"):
        win = "You win $50"
    if (slot1==slot2==slot3=="bar"):
        win = "You win $5"
    if (slot1="cherry")
       (slot2="crown")
       (slot3="bar"):
        win = "You win $1000"
    return slot1+":"+slot2+":"+slot3+" "+win
for i in range(int(numberOfTimes)):
    print(play())
