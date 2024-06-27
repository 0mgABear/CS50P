def main():
    time = input("What's the time? ") #get user input, always in 24 hour format
    timing = convert(time)
    if (7 <= timing and timing <= 8):
        print("breakfast time")
    elif (12 <= timing and timing <= 13):
        print("lunch time")
    elif (18 <= timing and timing <= 19):
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":") #splitting into 2 variables, putting it into convert variable rather than main variable
    hours, minutes = float(hours), float(minutes) #converting into integers
    output = hours + (minutes / 60)
    return output

if __name__ == "__main__":
    main()
