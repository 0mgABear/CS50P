import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        counter = 0
        while counter < 3:
            user_answer = input(f"{x} + {y} = ")
            try:
                if int(user_answer) == (x + y):
                    score += 1
                    break
                elif int(user_answer) != (x + y):
                    counter += 1
                    print("EEE")
            except ValueError:
                counter += 1
                print("EEE")
            if counter == 3:
                print(f"{x} + {y} = {x + y}")
                counter = 0
                break
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in (1, 2, 3):
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
