import random

def game(x):
    num = random.randint(1, x)
    guess = 0
    while guess != num:
        guess = int(input(f"enter a number between 1 and {x}: "))

        if guess < num:
            print("Too low!")
        elif guess > num:
            print("Too high!")
    print("Congrats! You got the correct number!")

# The computer guessing function was made with help of https://youtu.be/8ext9G7xspg
def computer_guess(x):
    low = 1
    high = x

    guess = 0
    feedback = ""
    while feedback != "e":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        print(guess)

        feedback = input("is your number higher (H), lower (L), or equal (E) to the guess? ").lower

        if feedback == "h":
            low = guess+1
        elif feedback == "l":
            high = guess-1

    print("The computer won!")

if input("do you want to guess a number? (y/n) ").lower == "y":
    game(int(input("What is the highest possible number? ")))

if input("Do you want the computer to guess? (y/n) ").lower == "y":
    computer_guess(int(input("What is the highest possible number? ")))