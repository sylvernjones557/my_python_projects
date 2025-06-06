import time

def pause():
    time.sleep(2)

# Intro ASCII Art
print(r'''
   _____                                         _   _             
  |_   _|                                       | | (_)            
    | | ___  _ __ ___  _ __ ___   __ _ _ __   __| |  _ _ __   __ _ 
    | |/ _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` | | | '_ \ / _` |
    | | (_) | | | | | | | | | | | (_| | | | | (_| | | | | | | (_| |
    \_/\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_| |_|_| |_|\__, |
                                                               __/ |
                                                              |___/ 
''')

print("Welcome to Treasure Island!")
pause()
print("Your mission is to complete this quest and find the hidden treasure.\n")
pause()

choice1 = input("Would you like to accept this mission?\n")
if choice1 == "yes" or choice1 == "YES":
    choice2 = input("Now you have a pothole of mystery path. Would you like to cross it or go your usual way? Yes or No\n")
    if choice2 == 'y' or choice2 == 'Y':
        print("You entered into the pothole... ahh... ah... Game Over! 💀")
    else:
        print("Wow! You chose the right path. Actually, you avoided a danger in your last step...")
        pause()
        choice3 = input("Now comes a lake before you. Would you like to swim across or wait for some time?\n")
        if choice3 == "swim" or choice3 == "SWIM":
            print(r'''
              ,-'`-.
           ,-'  __  `-.
          /   /  \_/  \ 
         |    \__/`\__/   - A SHARK APPEARS!
         \    (_) (_) /
          \          /
           `-.____.-'
''')
            print("Oh no... a shark ate you! You are out of the game. GAME OVER 🦈")
        else:
            print("Since you waited, you received a boat as a gift and used it to cross the lake. 🚣")
            pause()
            choice4 = input("Now here comes a bungalow. Would you like to go inside or wait outside? (GO or WAIT)\n")
            if choice4 == "wait" or choice4 == "WAIT":
                print(r'''
                       __
                      / _)
         .-^^^--._.-'/ /
      __/       `-' /    - ROAR! A DINOSAUR!
     <__.|_|-|_|-|_|
''')
                print("Oh no... a dinosaur ate you. Game Over! 🦖")
            else:
                print("You've reached the final level. There are only three rooms in front of you...")
                pause()
                print(r'''
 ______   ______   ______
|      | |      | |      |
|  RED | | BLUE | |YELLOW|
|______| |______| |______|
''')
                choice5 = input("Three doors are colored RED, BLUE, and YELLOW. Which one would you like to enter? (RED, BLUE, YELLOW)\n")
                if choice5 == "RED" or choice5 == "red":
                    print(r'''
     (  .      )
     )           (              )
           .  '   .   '  .  '  .
  (    , )       (.   )  (   ',    )
   .' ) ( . )    ,  ( ,     )   ( .
)( . )    ( . )  ( . )   (. )    ( )
''')
                    print("OH NO! You are burnt by fire. Game Over! 🔥")
                elif choice5 == "BLUE" or choice5 == "blue":
                    print(r'''
             _.-=-._     .--.
          o~`  '  >`.  / o  \ 
          `.  ,       \    /    - A BLUE BEAST!
           `-.-'    .-' '--'
''')
                    print("OH NO! A blue beast ate you. Game Over! 🐲")
                elif choice5 == "YELLOW" or choice5 == "yellow":
                    print(r'''
          _.+._     
        (^\/^\/^)
         \@*@*@/ 
         {_____}   - YOU FOUND THE TREASURE!
        /       \ 
      (| TREASURE|)
       \_______/
''')
                    print("HEY! YOU KNOW WHAT? YOU WON THE GAME! 🎉 CONGRATS, CHAMP! YOUR MISSION IS COMPLETE! 🏆")
                else:
                    print("You were too careless... and turned to ashes. Goodbye! 💨")
else:
    print("You fool! Get out of here. You have no courage to start this mission. Goodbye! 🏝️")
