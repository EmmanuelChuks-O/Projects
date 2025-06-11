# Python Slot Machine

import random

def spin_row():
    symbols = ["🎰", "🎮", "🎱", "🕹️"]

    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results

def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🎰":
            return bet * 3
        elif row[0] == "🎮":
            return bet * 4
        elif row[0] == "🎱":
            return bet * 5
        elif row[0] == "🕹️":
            return bet * 6
    return 0

def main():
    balance = 100

    print("***********************************")
    print("Welcome to Emmanuel's Slot Machine!")
    print("****** Symbols: 🎰 🎮 🎱 🕹️ ******")
    print("***********************************")

    while balance > 0:
        print(f"Your balance is ${balance}")

        bet = input("Place your bet amount:$ ")

        if not bet.isdigit():
            print("Please enter a valid amount.")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than zero.")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning....\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost this round")

        balance += payout

        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again != "Y":
            break

    print(f"Game over! Your final balance is ${balance}")

if __name__ == '__main__':
    main()

