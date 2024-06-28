def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    # Check if it starts with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Check length
    if len(s) < 2 or len(s) > 6:
        return False

    # Check for invalid characters and ensure numbers are at the end
    number_found = False
    for i, char in enumerate(s):
        if not char.isalnum(): #checking to make sure it's alphanumeric
            return False
        if char.isdigit():
            if char == '0' and not number_found:  # First number cannot be '0'
                return False
            number_found = True
        elif number_found:
            return False  # A letter appears after a number, which is invalid

    return True

main()
