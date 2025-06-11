# Hangman in Python
# from wordslist import words
import random

words = ("apple", "orange", "banana", "coconut", "pineapple", "berries")

# dictionary of key:(tuple)
hangman_art = {0: ("     ",
                   "     ",
                   "     "),
               1: ("  O  ",
                   "     ",
                   "     "),
               2: ("  O  ",
                   "  |  ",
                   "     "),
               3: ("  O  ",
                   " /|  ",
                   "     "),
               4: ("  O  ",
                   " /|\\",
                   "     "),
               5: ("  O  ",
                   " /|\\",
                   " /   "),
               6: ("  O  ",
                   " /|\\",
                   " / \\"), }

# for line in hangman_art[6]:
#     print(line)

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        # display_answer(answer)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("You entered a wrong guess.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed that letter {guess}")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for index in range(len(answer)):
             if answer[index] == guess:
                hint[index] = guess

        else:
            wrong_guesses+= 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You WIN!")
            is_running = False
        elif wrong_guesses >= len(hangman_art)- 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You LOSE!")
            is_running = False

if __name__ == '__main__':
    main()
