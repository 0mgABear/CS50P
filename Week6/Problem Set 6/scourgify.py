import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    inputfile = sys.argv[1]
    outputfile = sys.argv[2]

    try:
        with open(inputfile) as file:
            reader = csv.reader(file)
            header = next(reader)  # Skip the header row
            rows = []
            for row in reader:
                last, first = row[0].split(", ")
                house = row[1]
                rows.append([first, last, house])

        with open(outputfile, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["first", "last", "house"])
            writer.writerows(rows)

    except FileNotFoundError:
        sys.exit(f"Could not read {inputfile}")

if __name__ == "__main__":
    main()
