import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Define the regex pattern to match the input formats
    pattern = r"^(\d{1,2}(:\d{2})?) (AM|PM) to (\d{1,2}(:\d{2})?) (AM|PM)$"
    match = re.match(pattern, s)

    if not match:
        raise ValueError("Invalid format")

    start_time, _, start_period, end_time, _, end_period = match.groups()

    def to_24_hour(time, period):
        hours, minutes = (time.split(":") + ["00"])[:2]
        hours = int(hours)
        minutes = int(minutes)

        if period == "AM":
            if hours == 12:
                hours = 0
        elif period == "PM":
            if hours != 12:
                hours += 12

        if hours >= 24 or minutes >= 60:
            raise ValueError("Invalid time")

        return f"{hours:02}:{minutes:02}"

    start_24 = to_24_hour(start_time, start_period)
    end_24 = to_24_hour(end_time, end_period)

    return f"{start_24} to {end_24}"

if __name__ == "__main__":
    main()
