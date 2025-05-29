import random
import time
def pause():
    time.sleep(2)
word= ["banana", "engine", "python", "random", "coffee", "future"]
comp_choice = list(random.choice(word))  # The word to guess
hangman_stages = [
    '''
       +---+
       |   |
           |
           |
           |
           |
    =========
    ''',
    '''
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    ''',
    '''
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    ''',
    '''
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    ''',
    '''
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    ''',
    '''
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    ''',
    '''
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    '''
]

turn = 6
display = []
print("WELCOME TO THE HANGMAN GAME .......\n GUESS THE RIGHT WORD ......")
for i in range(len(comp_choice)):
    display += "_"
print("well you have a hint now you word has these many letters ")
print("".join(display))


game_over = False
while not game_over:
    print("*************************************************************************************")
    guess_letter = str(input("Guess a letter...\n"))
    for position in range(len(comp_choice)):
        if comp_choice[position] == guess_letter:
            print("yes your guess was right...")
            display[position] = guess_letter
    print(hangman_stages[6-turn])
    print("".join(display))
    pause()
    print("THINKING.........")



    if guess_letter not in comp_choice:
        pause()
        print("THINKING.........")
        print("no it is wrong...")
        print(''.join(display))
        turn -= 1
        print(hangman_stages[6-turn])
        print(f".................chances left {turn} / 6...........................")
        if turn == 0:
            print("*************************************************************************************")
            pause()
            print("THINKING.........")
            print("you have no chances left...")
            print(f"the correct word is...")
            print("".join(comp_choice))
            print(hangman_stages[6])
            print("GAME OVER...")
            print("*************************************************************************************")
            game_over = True

    if "_" not in display:
        print("*************************************************************************************")
        pause()
        print("THINKING.........")
        print("You have won the game")
        print(''.join(display))
        print("*************************************************************************************")
        game_over = True
