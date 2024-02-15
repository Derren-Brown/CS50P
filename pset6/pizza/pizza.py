import sys
from tabulate import tabulate
import csv

def main():
    if len(sys.argv) < 2:
        print("Too few arguments")
        sys.exit(1)
    if len(sys.argv) > 2:
        print("Too many arguments")
        sys.exit(1)
    if not sys.argv[1].endswith(".csv"):
        print("Not a csv file")
        sys.exit(1)
    table = []
    try:
        with open(sys.argv[1], "r") as f:
            reader = csv.DictReader(f)
            reader = list(reader)
            headers = reader[0].keys()
            headers = list(headers)
            for row in reader:
                table.append([row[headers[0]], row[headers[1]], row[headers[2]]])
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)
    else:
        print(tabulate(table, headers, tablefmt = "grid"))


if __name__ == "__main__":
    main()
