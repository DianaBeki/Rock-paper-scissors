import random

while True:
    player_input = input("Pick an option (Rock, Paper, or Scissors): ")
    possible_option = ['rock', 'paper', 'scissors']
    computer_selection = random.choice(possible_option)
    print(f"Player ({player_input}) : CPU ({computer_selection})")

    if player_input == computer_selection:
        print(f"Both players picked the same moves. It's a tie!")
    elif player_input == "rock":
        if computer_selection == "Scissors":
            print("Rock beats scissors! You win!")
        else:
            print("Paper beats rock! You lose.")
    elif player_input == "paper":
        if computer_selection == "rock":
            print("Paper beats rock! You win!")
        else:
            print("Scissors beats paper! You lose.")
    elif player_input == "scissors":
        if computer_selection == "paper":
            print("Scissors beats paper! You win!")
        else:
            print("Rock beats scissors! You lose.")
    else:
        print("Error! Please try again")
    
    play_again = input("Want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break