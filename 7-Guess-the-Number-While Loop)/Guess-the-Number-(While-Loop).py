import random

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)

# Initialize user guess
user_guess = None

# Loop until the user guesses correctly
while user_guess != random_number:
    try:
        # Ask the user for a guess
        user_guess = int(input("Guess the number (1-10): "))

        # Check if the guess is within the valid range
        if user_guess < 1 or user_guess > 10:
            print("Please enter a number between 1 and 10.")
            continue

        # Give feedback on the guess
        if user_guess < random_number:
            print("Too low, try again!")
        elif user_guess > random_number:
            print("Too high, try again!")
        else:
            print("Correct! 🎉")
    except ValueError:
        # Handle non-integer input
        print("Invalid input. Please enter a valid number.")
