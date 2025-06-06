import random
import time
import os

# Clear screen function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Card drawing function
def cards_throw():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)

# Score calculation with Ace adjustment
def calci_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    while 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Compare final scores
def compare(player_score, dealer_score, name):
    if player_score == dealer_score:
        return "🤝 IT'S A DRAW!"
    elif dealer_score == 0:
        return "😱 DEALER WINS WITH BLACKJACK!"
    elif player_score == 0:
        return f"🎉 {name.upper()} WINS WITH BLACKJACK!"
    elif player_score > 21:
        return f"💥 {name.upper()} BUSTED... YOU LOSE!"
    elif dealer_score > 21:
        return "🔥 DEALER BUSTED... YOU WIN!"
    elif player_score > dealer_score:
        return f"🏆 {name.upper()} WINS!"
    else:
        return "😤 DEALER WINS!"

# Display hand nicely
def display_hand(title, hand, score, hide_second=False):
    print(f"\n{title}'s Hand: ", end="")
    for i, card in enumerate(hand):
        if hide_second and i == 1:
            print("[??]", end=" ")
        else:
            print(f"[{card}]", end=" ")
    print(f"| Score: {'??' if hide_second else score}")

# Game starts here
def play_game():
    clear()
    print(r"""
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                      _/ |                
                     |__/                 
    """)
    print("🎲 WELCOME TO THE BLACKJACK GAME 🎲")
    time.sleep(1)

    name = input("Enter your name player: ").capitalize()
    print(f"\n✨ WELCOME {name}! Get ready... ✨\n")
    time.sleep(1)

    player = []
    dealer = []

    for _ in range(2):
        player.append(cards_throw())
        dealer.append(cards_throw())

    game_over = False
    while not game_over:
        player_score = calci_score(player)
        dealer_score = calci_score(dealer)

        display_hand(name, player, player_score)
        display_hand("Dealer", dealer, dealer_score, hide_second=True)

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            choice = input(f"\n{name}, do you want to [hit] or [stand]? ").lower()
            if choice == "hit":
                player.append(cards_throw())
                time.sleep(1)
            else:
                game_over = True

    # Dealer's turn
    print("\n🃏 Dealer's Turn...\n")
    time.sleep(1)
    while calci_score(dealer) < 17:
        dealer.append(cards_throw())
        time.sleep(1)

    player_final_score = calci_score(player)
    dealer_final_score = calci_score(dealer)

    display_hand(name, player, player_final_score)
    display_hand("Dealer", dealer, dealer_final_score)

    print("\n" + compare(player_final_score, dealer_final_score, name))
    print("🎮 Game Over 🎮\n")

# Play loop
while True:
    play_game()
    again = input("Do you want to play again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for playing! Goodbye 👋")
        break
