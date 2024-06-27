def main():
    user_input = input("Please enter a string: ")
    str_user_input = str(user_input) #converting it to a string
    print(convert(str_user_input))

def convert(input: str):
    input = input.replace(":)", "🙂")
    input = input.replace(":(", "🙁")
    return input

main()

