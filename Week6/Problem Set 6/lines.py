import sys

def main():
    # Check if the number of command-line arguments is exactly one
    if len(sys.argv) < 2:
        sys.exit("Too few command-line argumetns")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line argumetns")

    filename = sys.argv[1]
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(filename) as file:
            lines = 0
            for line in file:
                stripped_line = line.strip()
                if stripped_line and not stripped_line.startswith("#"):
                    lines += 1
            print(lines)
    except FileNotFoundError:
        sys.exit("File not found")

if __name__ == "__main__":
    main()

