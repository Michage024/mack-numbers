# src/main.py

import random

def play_game():
    number_to_guess = random.randint(1, 10)
    attempts = 0
    max_attempts = 5
    guessed = False

    print("\nWelcome to 'Mack Electro Number' game!")
    print(f"I have selected a number between 1 and 10. You have {max_attempts} attempts to guess it.")
    
    while not guessed and attempts < max_attempts:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid integer.")
    
    if not guessed:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
