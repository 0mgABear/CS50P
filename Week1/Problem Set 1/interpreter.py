import operator

def main():
    user_input = input("Expression: ")
    x, y, z = user_input.split(" ")
    x , z = int(x), int (z)

    math_operations = {
        "+" : operator.add,
        "-" : operator.sub,
        "*" : operator.mul,
        "/" : operator.truediv
    }

    if y in math_operations:
        # no need division by zero checking since it's already stated in the assumptions :)
        result = math_operations[y](x, z)
        print(f"{result:.1f}")
    else:
        print("Invalid operator")

main()

