import sys


def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    if not sys.argv[1].endswith(".py"):
        print("Not a Python file")
        sys.exit(1)
    val = 0
    try:
        with open(sys.argv[1], "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.lstrip()
                if not line == "":
                    if not line[0] == "#":
                        val += 1
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)
    else:
        print(val)


if __name__ == "__main__":
    main()
