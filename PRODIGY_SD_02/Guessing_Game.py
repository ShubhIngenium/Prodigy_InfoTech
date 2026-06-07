import random


def main():
    print("Guessing Game")
    print("I am thinking of a number between 1 and 100.")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        attempt_input = input("Enter your guess: ").strip()
        attempts += 1

        if not attempt_input.isdigit():
            print("Please enter a valid whole number.")
            continue

        guess = int(attempt_input)

        if guess < secret_number:
            print("Too low. Try again.")
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print(f"Correct! The number was {secret_number}.")
            print(f"You guessed it in {attempts} attempt{'s' if attempts != 1 else ''}.")
            break


if __name__ == "__main__":
    main()
