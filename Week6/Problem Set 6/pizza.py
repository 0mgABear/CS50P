import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a csv file")

    try:
        with open(sys.argv[1], newline='') as file:
            reader = csv.reader(file)
            header = next(reader)
            rows = [row for row in reader]
            print(tabulate(rows, headers=header, tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File not found!")

if __name__ == "__main__":
    main()
