def main():
    groceries = {}
    while True:
        try:
            item = input().strip().upper() #taking user input and converting it into upper case
            print()
            if item in groceries:
                groceries[item] += 1
            else:
                groceries[item] = 1
        except EOFError:
            sorted_groceries = sorted(groceries.items())
            for item, count in sorted_groceries:
                print(f"{count} {item}")
            break

main()

