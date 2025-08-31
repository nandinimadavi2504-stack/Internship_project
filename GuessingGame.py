import random

print("Number Guessing Game")
print("I have picked a number between 1 and 100.")
print("You have 10 attempts to guess it.")

secret_number = random.randint(1, 100)
attempts = 10

# Debug mode: set True to see the number, False to hide
DEBUG = True
if DEBUG:
    print("Debug: Secret number is", secret_number)

for i in range(1, attempts + 1):
    guess_input = input(f"Attempt {i}: Enter your guess: ")

    if not guess_input.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess_input)

    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print(f"Congratulations! You guessed it in {i} attempts.")
        break
else:
    print(f"Game over. The number was {secret_number}.")
