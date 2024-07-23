from pyfiglet import Figlet
import sys
import random

def main():
    figlet = Figlet()
    if len(sys.argv) not in (1, 3):
        sys.exit("Invalid usage")

    # No arguments provided, use a random font
    if len(sys.argv) == 1:
        font_list = figlet.getFonts()
        figlet.setFont(font=random.choice(font_list))

    # Specific font requested
    elif len(sys.argv) == 3 and (sys.argv[1] in ("-f", "--font")):
        if sys.argv[2] in figlet.getFonts():
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Invalid usage")

    # Invalid argument structure
    else:
        sys.exit("Invalid usage")

    user_input = input("Input: ")
    print(figlet.renderText(user_input))

if __name__ == "__main__":
    main()
