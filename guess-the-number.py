import random

# Function to generate a random number between 1 and 100
def generate_random_number():
    return random.randint(1, 100)

# Main function to play the game
def main():
    print("Welcome to the Guess the Number Game!")
    print("I have selected a random number between 1 and 100.")

    random_number = generate_random_number()
    attempts = 0

    while True:
        guess = input("Enter your guess (1-100): ")

        try:
            guess = int(guess)
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
            elif guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {random_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
