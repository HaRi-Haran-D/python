print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("You're at the cross road, What direction do you want to Go? 'Right' or 'Left'").lower()
if direction == "right":
    print("You have came to a Lake. There is Island in the middle of the lake.")
    action = input("Type 'wait' to wait for a boat or type 'swim' to swim across").lower()
    if action == "wait":
        print("You have arrived to the island unharmed")
        color = input("There is a house with 3 doors, one with 'Red' one with 'Yellow' one with 'Blue' Which one do you want to choose?").lower()
        if color == "red":
            print("You found the Treasure! You Win!.")
        elif color == "Yellow" or color == "yellow":
            print("Sorry you have stepped into a lion's cage, Game Over")
        else:
            print("Sorry you have fallen into their trap, Game Over")
    else:
        print("Sorry but you have been killed by piranhas, Game Over.")
else:
    print("Sorry, you fall into a Deep hole. Game Over.")
