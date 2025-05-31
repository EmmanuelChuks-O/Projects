# loop
import random

while True:
    choice = input("Roll the dice? (y/n): ") # ask user: roll the dice?
    if choice == "y" or choice == "Y" : # if user enters y or Y
        die1 = random.randint(1, 6) # generate two random numbers
        die2 = random.randint (1, 6) # generate two random numbers
        print(f'({die1}, {die2})') # print the random numbers
    elif choice == "n" or choice == "N" : # if user enters n
        print("Thanks for playing!") # print thank for playing
        break
    else:
        print("Invalid choice!")
# else
# terminate
# print invalid choice

