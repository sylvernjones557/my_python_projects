import random
import time
def pause():
    time.sleep(1.5)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock,paper,scissors]
replay = "yes"
print("WELCOME TO ROCK PAPER SCISSOR GAME")
pause()
print("*********************************************************************************\n***************************************************************")
name = input("PLEASE ENTER YOUR NAME...")
while replay == "yes":
    print(f"WELCOME {name}")
    user_input = int(input("enter your choice 0 for RoCk ... 1 for PaPer ... 2 FOR SciSsOr\n"))
    pause()
    if user_input == 0 or user_input == 1 or user_input == 2:
        print("********************************************************************************")
        print(f"{name} CHOOSE \n{game[user_input]}")
        comp_choice = random.randint(0, 2)
        print("********************************************************************************")
        print(f"COMPUTER CHOOSE \n{game[comp_choice]}")
        pause()
        if comp_choice == user_input:
            print("That's a draw start again...")
        elif (user_input == 0 and comp_choice == 2) or (user_input == 1 and comp_choice == 0) or (
                user_input == 2 and comp_choice == 1):
            print(f"{name} WINS")
        else:
            print("COMPUTER WINS.....")
    else:
        pause()
        print("INVALID INPUT ... \n INPUT SHOULD BE 0 OR 1 OR 2...")
    replay = input("DO YOU WANT TO REPLAY AGAIN ... ENTER YES OR SOME OTHER OTHER KEY TO QUIT....").lower()
print("THANK YOU ....HAVE A NICE DAY !!!")