import random

def number_guessing_game():


    target_number = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100.\n")

    while True:
        try:

            user_guess = int(input("Enter your guess: "))
            attempts += 1


            if user_guess < target_number:
                print("Too low!\n")
            elif user_guess > target_number:
                print("Too high!\n")
            else:

                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break

        except ValueError:

            print("Invalid input! Please enter a valid integer.\n")


number_guessing_game()
