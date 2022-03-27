import random as rand

choices = ["R", "P", "S"]

def RPS():
    computer_choice = rand.choice(choices)
    player_choice = input("Enter either Rock (R), Paper (P), or Scissors (S): ").upper()

    if player_choice in choices:
        print(f"{player_choice} Vs {computer_choice}")
        if choices[choices.index(player_choice) - 1] == computer_choice:
            return "Player wins!" 
        elif choices[choices.index(player_choice) - 2] == computer_choice:
            return "Computer wins!"
            
        return "Tie!"

print(RPS())