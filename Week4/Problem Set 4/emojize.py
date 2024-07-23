import emoji

def main():
    emoji_input = input("Input: ")
    # Extract the emoji part
    emoji_shortcode = emoji_input.strip()  # Remove leading/trailing spaces

    try:
        print(emoji.emojize(emoji_shortcode, language='alias'))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
