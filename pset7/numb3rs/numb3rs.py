import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"(.+)\.(.+)\.(.+)\.(.+)", ip):
        for i in range(4):
            try:
                if 0 <= int(matches.group(i+1)) <= 255:
                    pass
                else:
                    return False
            except ValueError:
                return False
    else:
        return False
    return True

if __name__ == "__main__":
    main()