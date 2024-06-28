def main():
    camelCase = input("Camelcase: ") # get user input for camelCase
    snake_case = ""
    for c in camelCase: # iterate through the string
        if c.isupper(): # do some form of checking to check if it is smaller or upper case
            snake_case += "_" + c.lower() # if it is upper case - change it to smaller case and insert an underscore (_) in front
        else:
            snake_case += c
    print(snake_case)

main()

