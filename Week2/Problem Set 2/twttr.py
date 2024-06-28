def main():
    user_input = input("Input: ")
    output = []
    vowels = set("aeiouAEIOU")
    for c in user_input:
        if c not in vowels:
            output.append(c)
    print("".join(output))

main()
