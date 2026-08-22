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
print (" you are at a cross road. Where do you want to go?")
choice1 = input( "     Type 'Left' or 'Right'\n")
if choice1=="Left":
    print("you have come to Lake. There is an island in the middle of the Lake.")
    choice2 = input("Type 'wait' to wait for the boat, Type 'swim' to swim across\n")
    if choice2 == "wait":

       print("You have arrived to an island unharmed . There is a house with 3 doors.")
       choice3=input( "\n  1) RED   2)YELLOW   3)BLUE  Which colour do you choose?\n")
       if choice3=="RED":
            print("You are burned by fire\n __GAME__OVER__")
       elif  choice3=="YELLOW":
            print("You win!!!! Congratulations")
       elif choice3=="BLUE":
            print("You are eaten by beasts\n __GAME__OVER__")
    else:
        print("You are attacked by trout\n __GAME__OVER__")
else :
    print("you have fallen into a hole\n __GAME__OVER__")
