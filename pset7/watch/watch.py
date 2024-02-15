import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(r".*\"https?://(?:www\.)?youtube\.com/embed/(\w+)\".*", s)
    if matches:
        short = matches.group(1)
        return f"https://youtu.be/{short}"
    return "None"


if __name__ == "__main__":
    main()
