# Python Banking Program

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter amount to deposit: "))

    if amount < 0:
        print("Deposit cannot be less than zero.")
        return 0
    else:
        return amount

def withdraw(balance):
    withdraw_amount = float(input("Enter amount to withdraw: "))

    if withdraw_amount > balance:
        print("You don't have enough balance.")
        return 0
    elif withdraw_amount < 0:
        print("Amount must be greater than 0 to withdraw.")
        return 0
    else:
        return withdraw_amount



def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking Program")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("That is not a valid choice")

    print("Thank you and have a nice day!")

main()

