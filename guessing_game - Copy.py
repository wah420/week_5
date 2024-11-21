import random

def guessing_game():
    """
    This function implements a number guessing game where the user has to guess a randomly generated number between 0 and 10.

    The function performs the following steps:
    1. Generates a random number between 0 and 10 (inclusive) that the user needs to guess.
    2. Continuously prompts the user to enter their guess.
    3. Compares the user's guess with the generated number and provides feedback:
       - If the guess is correct, it prints a congratulatory message and exits the loop.
       - If the guess is too low, it informs the user that their guess is too low.
       - If the guess is too high, it informs the user that their guess is too high.
    4. Repeats this process until the user correctly guesses the number.
    """    
    answer = random.randint(0, 10)  # Generate a random number between 0 and 10

    # Step 3: Start a loop to allow the user to keep guessing
    while True:
        # Step 4: Prompt the user for a guess
        guess = int(input("Guess a number between 0 and 10: "))

        # Step 5: Check if the guess is correct, too low, or too high
        if guess == answer:
            print(f"Right! The answer is {answer}")
            break  # Exit the loop since the guess is correct
        elif guess < answer:
            print(f"Your guess of {guess} is too low!")
        else:  # guess > answer
            print(f"Your guess of {guess} is too high!")

# Test your code:
guessing_game()
