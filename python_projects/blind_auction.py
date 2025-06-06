import os
import time


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_banner():
    print(r"""
   ____  _     _           _       _                 
  |  _ \| |__ (_) ___  ___| | __ _| |_ ___  _ __ ___ 
  | |_) | '_ \| |/ _ \/ __| |/ _` | __/ _ \| '__/ _ \
  |  __/| | | | |  __/ (__| | (_| | || (_) | | |  __/
  |_|   |_| |_|_|\___|\___|_|\__,_|\__\___/|_|  \___|

    """)
    print("🏆 Welcome to the BLIND AUCTION! 🏆\n")
    print("All bids are secret 🤫, highest bidder takes the prize! 🏅")
    print("Let the bidding war begin! 💼🔐\n")
    print("=" * 55)


def pause_with_message(message, seconds=2):
    print(message)
    time.sleep(seconds)


def main():
    clear_screen()
    print_banner()

    auctioneers_entry = []

    while True:
        name = input("🚀 Enter your name, brave bidder: ").strip()
        while True:
            bid_input = input("💰 Enter your bid amount (₹): ").strip()
            if bid_input.isdigit() and int(bid_input) > 0:
                bid_amt = int(bid_input)
                break
            else:
                print("⚠️  Invalid input! Please enter a positive number.")

        auctioneers_entry.append({"name": name, "bid_amt": bid_amt})

        choice = input("\nIs there another bidder ready to challenge? (yes/no): ").strip().lower()
        if choice == "yes":
            pause_with_message("\nPrepare yourselves... Next bidder coming up!\n", 3)
            clear_screen()
            print_banner()
        else:
            pause_with_message("\n🛑 The bidding has closed! Let's see who took the crown...\n", 3)
            break

    # Find the highest bid
    winner = max(auctioneers_entry, key=lambda x: x["bid_amt"])

    trophy_art = r"""
          ___________
         '._==_==_=_.'
         .-\:      /-.
        | (|:.     |) |
         '-|:.     |-'
           \::.    /
            '::. .'
              ) (
            _.' '._
           `"""""""`

    """

    print(trophy_art)
    print(f"🎉 Congratulations, {winner['name']}! 🎉")
    print(f"You have won the blind auction with a bid of ₹{winner['bid_amt']}!\n")
    pause_with_message("Thanks to all bidders for playing fair and square! 🤝", 3)


if __name__ == "__main__":
    main()
