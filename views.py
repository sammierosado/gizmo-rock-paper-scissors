# views.py should have barely anything more than print and input statements

def prompt_player():
    print("Welcome to Rock, Paper, Scissors.")
    print("Please choose rock, paper, scissors. Or Exit to quit")
    print()

def get_player_input():
    return input(": ").strip().lower()

def bad_input():
    print("Choice not recognized.")

def welcome():
    print("Welcome to Rock, Paper, Scissors")

def display_win(choice, computer_choice):
    print(f"{choice} beats {computer_choice}, you win.")

def display_tie(choice, computer_choice):
    print(f"{choice} and {computer_choice} are a tie.")

def display_loss(choice, computer_choice):
    print(f"{choice} loses to {computer_choice}.")
