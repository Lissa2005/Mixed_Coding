import random

def choice_cave():
    outcome = random.choices(["Gobbles you Down!","Greets you before sharing his Treasure"])
    return(outcome)

#main programs
print("You are in the Kingdom of Dragons.\nIn front of you, you see two caves.","\nIn one cave, the dragon is friendly and will \nshare his treasure with you.\nThe other dragon is hungry and will eat you on sight!")
val = input("\nCave 1 or 2: ")
while val not in ["1","2"]:
    val = input ("Cave 1 or 2: ")

print("You approach the cave...\nA large Dragon jumps out in front of you!\nHe opens his jaws and...\n")
print()
outcome=choice_cave()
print(outcome)