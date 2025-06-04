import random

options = ("rock", "paper", "scissors")
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    else:
        print("Computer wins and you lose!")

    # or
    # elif computer == "rock" and player == "scissors":
    #     print("Computer wins and you lose!")
    # elif computer == "scissors" and player == "paper":
    #     print("Computer wins and you lose!")
    # elif computer == "paper" and player == "rock":
    #     print("Computer wins and you lose!")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if not play_again == "y":
        running = False

    # or
    # if not input("Do you want to play again? (y/n): ").lower() == "y":
    #     running = False

    print("Thank you for playing!")
