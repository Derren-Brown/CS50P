from validator_collection import validators, checkers


def main():
    s = input("What's your email address? ")
    is_valid = checkers.is_email(s)
    if is_valid:
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
