from random import randrange

import views

def evaluate_match(player_choice, computer_choice):
    """ return 'win', 'loss', or 'tie' depending on the match """
    if player_choice == "rock":
        if computer_choice == "rock":
            return "tie"
        elif computer_choice == "paper":
            return "loss"
        else:
            return "win"
    
    elif player_choice == "paper":
        if computer_choice == "rock":
            return "win"
        elif computer_choice == "paper":
            return "tie"
        else:
            return "loss"
    elif player_choice == "scissors":
        if computer_choice == "rock":
            return "loss"
        elif computer_choice == "paper":
            return "win"
        else:
            return "tie"

# def get_player_choice():
#     while True:
#         print("Pick rock, paper, or scissors")
#         choice = input(": ").strip().lower()
#         if choice in ("rock", "paper", "scissors"):
#             return choice
#         else:
#             print("Choice not recognized")

def get_computer_choice():
    """ return a random choice from 'rock', 'paper', or 'scissors' """
    computer_choice = randrange(3)
    return ("rock", "paper", "scissors")[computer_choice]

def main():
    views.welcome
    choice = views.get_player_input()
    computer_choice = get_computer_choice()
    result = evaluate_match(choice, computer_choice)

    games = 0
    wins = 0
    loss = 0
    tie = 0

    if result == "win":
        views.display_win(choice,computer_choice)
        wins +=1
        print(f"{choice} beats {computer_choice}, you win")
    elif result == "tie":
        tie += 1
        print(f"{choice} and {computer_choice} are a tie")
    else:
        print(f"{choice} loses to {computer_choice}, you lose")
        loss +=1
    games +=1

if __name__ == "__main__":

    main()