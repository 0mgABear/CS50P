import random

def main():
    # Prompt the user for a level until a positive integer is provided
    while True:
        try:
            prompt = input("Level: ")
            level = int(prompt)
            if level > 0:
                break
        except ValueError:
            pass

    # Randomly generate an integer between 1 and the specified level (inclusive)
    secret_number = random.randint(1, level)

    # Prompt the user to guess the number
    while True:
        try:
            guess = input("Guess: ")
            guess = int(guess)
            if guess <= 0:
                continue

            if guess < secret_number:
                print("Too small!")
            elif guess > secret_number:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            pass

if __name__ == "__main__":
    main()
