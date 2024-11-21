import random

def rock_paper_scissors_game():
    """
    Plays a Rock-Paper-Scissors game between the user and the computer.
    
    The user is prompted to enter 'rock', 'paper', or 'scissors'.
    The computer randomly chooses one of the three options.
    The winner is determined based on the standard rules of the game.
    The game continues until the user decides to quit by entering 'quit'.
    """

    while True:

        user_choice = input("Please choose between rock, paper, or scissors (or type 'quit' to exit): ").lower()

        if user_choice == 'quit':
            print("Now exiting the game")
            break

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid input. Please choose between rock, paper, or scissors.")
            continue

        computer_choice = random.choice(["rock", "paper", "scissors"])

        print(f"You chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win!")
        else:
            print("You lose!")

# Run the game
rock_paper_scissors_game()
