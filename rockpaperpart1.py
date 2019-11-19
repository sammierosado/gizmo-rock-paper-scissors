from random import randrange

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
    elif player_choice == "Exit":
        return 
        

def get_player_choice():
    while player_choice is not "Exit":
        print("Pick rock, paper, or scissors. Or Exit when finished with game.")
        choice = input(": ").strip().lower()
        if choice in ("rock", "paper", "scissors","Exit"):
            return choice
        else:
            print("Choice not recognized")

def get_computer_choice():
    """ return a random choice from 'rock', 'paper', or 'scissors' """
    computer_choice = randrange(3)
    return ("rock", "paper", "scissors")[computer_choice]

def main():
    
    print("Welcome to Rock, Paper, Scissors")
    print()
    choice = get_player_choice()
    computer_choice = get_computer_choice()
    result = evaluate_match(choice, computer_choice)
    while choice is not "Exit":
        if result == "win":
            print(f"{choice} beats {computer_choice}, you win")
        elif result == "tie":
            print(f"{choice} and {computer_choice} are a tie")
        else:
            print(f"{choice} loses to {computer_choice}, you lose")

if __name__ == "__main__":
    main()
        