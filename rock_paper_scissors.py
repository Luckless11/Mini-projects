import random as rand

choices = ["Rock", "Paper", "Scissors"]

playing = True

while playing:
    computer_choice = rand.choice(choices)
    player_choice = input("Enter either Rock, Paper, or Scissors: ")

    if player_choice in choices:
        print(f"{player_choice} Vs {computer_choice}")
        if choices[choices.index(player_choice) - 1] == computer_choice:
            print("Player wins!") 
        elif choices[choices.index(player_choice) - 2] == computer_choice:
            print("Computer wins!")
        else:
            print("Tie!")
    
    if input("Do you want to play again? (y or n) ") == "n":
        playing = False