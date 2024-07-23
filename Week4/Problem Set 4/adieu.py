import inflect
import sys

def main():

    p = inflect.engine()

    print("Please enter names, one per line. Press Ctrl-D (or Ctrl-Z on Windows) to finish.")
    names = []
    while True:
        try:
            name = input()
            names.append(name)
        except EOFError:
            break

    farewell_message = construct_farewell_message(names, p)
    print(farewell_message)

def construct_farewell_message(names, p):
    if len(names) == 0:
        return ""

    names_str = p.join(names)
    return f"Adieu, adieu, to {names_str}"

if __name__ == "__main__":
    main()
