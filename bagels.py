# bagels.py 
# In Bagels, a deductive logic game, you
# must guess a secret three-digit number
# based on clues. The game offers one of
# the following hints in response to your guess:
# “Pico” when your guess has a correct digit in the
# wrong place, “Fermi” when your guess has a correct
# digit in the correct place, and “Bagels” if your guess
# has no correct digits. You have 10 tries to guess the
# secret number.
import random

def greeting():
    print('''Bagels, a deductive logic game.
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:  That means:
    Pico        One digit is correct but in the wrong position.
    Fermi       One digit is correct and in the right position.
    Bagels      No digit is correct.''')

def hint(guess, number):
    flag = 0
    for x in range(0,3):
        if guess[x] == number [x]:
            print("Fermi")
            flag = 1
    for x in range(0,3):
        for y in range(0,3):
            if (guess[x] == number[y]) and (x != y):
                print("Pico")
                flag = 1
    if flag == 0:
        print("Bagels")
    
if __name__ == "__main__":
    # Initializations
    play = "yes"
    guess = ""
    guess_continue = True
    count = 0

    greeting()
    while play.upper() != "NO":
        print("I have thought up a number.")
        print(" You have 10 guesses to get it.")
        number = str(random.randint(0, 999))
        while (guess_continue):
            count = count + 1
            guess = input(f"{number}, Guess #{count} :> ")  
            if guess != number:
                hint(guess, number)
                guess_continue = True
            if guess == number:
                guess_continue = False
                print("You got it!")
            if count > 10:
                guess_continue = False  
        play = input("Continue Playing? (yes or no) :> ")
        if play.upper() == "YES":
            guess_continue = True
            count = 0
