def main():
    greeting = input("Please input a greeting: ")
    greeting_converted = greeting.strip().lower()
    if len(greeting_converted) == 0:
        print("$100")
    elif greeting_converted[:5] == "hello":
        print("$0")
    elif greeting_converted[0] == "h":
        print("$20")
    else:
        print("$100")


main()
