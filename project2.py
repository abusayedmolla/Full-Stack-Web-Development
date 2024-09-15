from random import choice
import random

for num in range(1, 101):
    def main():
            print("Welcome to the Number Guessing Game!")
            print("Try to guess the number between 1 and 100.")
            new = random.randint(1, 100)
            attempts = 0
            while True:
                choicee = int(input("\nEnter your guess:"))
                attempts +=1

                if choicee == new:
                    print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                elif choicee > new:
                    print('Too high!')
                elif choicee < new:
                    print('Too low!')




if __name__ == "__main__":
    main()