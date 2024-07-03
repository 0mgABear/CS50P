months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def main():
    while True:
        prompt = input("Date: ").strip()

        # Check for MM/DD/YYYY format
        if '/' in prompt:
            parts = prompt.split('/')
            try:
                month, day, year = map(int, parts)
                if 1 <= month <= 12 and 1 <= day <= 31:
                    break
            except ValueError:
                pass  # Continue to next check
        elif ',' in prompt:
            parts = prompt.replace(',', '').split()
            if parts[0] in months and parts[1].isdigit():
                try:
                    month = months.index(parts[0]) + 1
                    day = int(parts[1])
                    year = int(parts[2])
                    if 1 <= day <= 31 and year > 0:  # Check for positive year
                        break
                except ValueError:
                    pass  # Continue to next check

    output = f"{year:0>4}-{month:0>2}-{day:0>2}"
    print(output)

main()
