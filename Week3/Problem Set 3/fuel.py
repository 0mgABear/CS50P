def main():
    while True:
        try:
            fraction = input("Fraction: ")
            a, b = fraction.split("/") #splitting text
            a,b = int(a), int(b) #converting to integers

            if a > b:
                continue
            result = round(a / b * 100)

            if result >= 99:
                print("F")
            elif result <= 1:
                print("E")
            else:
                print(f"{result}%")
            break  # Exit the loop once a valid input is processed
        except (ValueError, ZeroDivisionError):
            continue  # Prompt the user again if an exception occurs

main()
