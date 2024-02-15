import requests
import sys


def main():
    if len(sys.argv) < 2:
        print("Missing command-line argument")
        sys.exit(1)
    try:
        n = float(sys.argv[1])
    except ValueError:
        print("Command line argument is not a number")
        sys.exit(1)
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        print("Request error")
        sys.exit(1)
    try:
        r = r.json()
    except ValueError:
        print("Not json file")
    else:
        rate = r["bpi"]["USD"]["rate_float"]
        print(f"${n * rate:,.4f}")


if __name__ == "__main__":
    main()
