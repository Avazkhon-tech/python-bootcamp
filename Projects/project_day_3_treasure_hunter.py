print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************''')

print('Welcome to Treasure island. \nYour misson is to find the treasure')

choice_1 = input("Left or right: ").lower()
if choice_1 == 'left':
    choice_2 = input('Swim or wait: ').lower()
    if choice_2 == 'wait':
        print('You have 3 doors. Red, Blue, Yellow')
        choice_3 = input('Which door: ').lower()
        if choice_3 == 'yellow':
            print('You win!')
        elif choice_3 == 'blue':
            print("Eaten by beasts. Game over. ")
        elif choice_3 == 'red':
            print('Burned by fire. Game over.')
        else:
            print('Game over')
    else:
        print("Attacked by trout. Game over.")
else:
    print("You fell into a hole. Game over.")




