def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollars = d[1:]
    dollars_float = float(dollars)
    return round(dollars_float, 1)

def percent_to_float(p):
    percent = p[:-1]
    percent_float = float(percent) / 100
    return percent_float

main()

