# 1st version
# import random
# while True:
#     user = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors. \n >>"))
#     if user > 2 or user < 0:
#         print("invalid number. Enter again")
#     else:
#         break
# computer = random.randint(0, 2)
# rock = """
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """
# paper = """
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """
# scissors = """
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """
# gestures = [rock, paper, scissors]
#
# print("Computer chose \n", gestures[computer])
# print("You chose \n", gestures[user])
# loose = 'You loose'
# win = 'You won'
# draw = 'draw'
# if user == 0 and computer == 0:
#     print(draw)
# elif user == 0 and computer == 1:
#     print(loose)
# elif user == 0 and computer == 2:
#     print(win)
# elif user == 1 and computer == 0:
#     print(win)
# elif user == 1 and computer == 1:
#     print(draw)
# elif user == 1 and computer == 2:
#     print(loose)
# elif user == 2 and computer == 0:
#     print(loose)
# elif user == 2 and computer == 1:
#     print(win)
# elif user == 2 and computer == 2:
#     print(draw)

# 2nd version. to use 2nd version lock the 1st version and unlock the 2nd.
# otherwise two versions will run at the same time
import random
while True:
    user = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors. \n >>"))
    if user > 2 or user < 0:
        print("invalid number. Enter again")
    else:
        break
computer = random.randint(0, 2)
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
gestures = [rock, paper, scissors]
print("Computer chose \n", gestures[computer])
print(computer)

print("You chose \n", gestures[user])
loose, win, draw = 'You loose', 'You won', 'draw'
if (user == 0 and computer == 1) or (user > computer):
    print(win)
elif user == computer:
    print(draw)
else:
    print(loose)






