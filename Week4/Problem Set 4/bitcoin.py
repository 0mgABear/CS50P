import requests
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python bitcoin.py <number_of_bitcoins>")

    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Raise an error for bad HTTP status codes
        data = response.json()
        price = data['bpi']['USD']['rate_float']
        cost = amount * price
        print(f"${cost:,.4f}")
    except requests.RequestException:
        sys.exit("Error fetching data from CoinDesk API")

if __name__ == "__main__":
    main()

