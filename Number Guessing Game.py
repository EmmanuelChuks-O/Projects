# Python number guessing game

import random

lowest_number = 1
highest_number = 10
answer = random.randint(lowest_number,highest_number)
guesses = 0
is_running = True


print("Python Number Guessing Game")
print(f"Please select a number between {lowest_number} and {highest_number}")

while is_running:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < lowest_number or guess > highest_number:
            print("That number is out of range ")
            print(f"Please select a number between {lowest_number} and {highest_number}")
        elif guess < answer:
            print("Your guess is too low! Try again")
        elif guess > answer:
            print("Your guess is too high! Try again")
        else:
            print(f"Your guess is right! We both guessed: {answer}")
            print(f"Well it took you {guesses} guesses")
            is_running = False
    else:
        print("Invalid guess")
        print(f"Please select a number between {lowest_number} and {highest_number}")




