import random


still_playing = True

while still_playing:
    limit = int(input("what do you want the highest possible number to be?: "))
    num = random.randint(1, limit)
    guess = int(input(f"enter a number between 1 and {limit}: "))

    if guess == num:
        print("congrats! you got the correct number!")
    else:
        print(f"uh-oh! the correct number was {num}, better luck next time!")
    
    play_again = input("do you want to play again? (y or n):")
    
    if play_again == "n":
        still_playing = False