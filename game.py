import random

def number_guessing_game():
    number = random.randint(1, 100)
    guess = 0
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100.")

    while guess != number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("Too low. Guess again.")
            elif guess > number:
                print("Too high. Guess again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"Congratulations! You guessed the number in {attempts} attempts.")

number_guessing_game()