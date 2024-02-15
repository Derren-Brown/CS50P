def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 1 < len(s) < 7:
        if s.isalnum():
            if s[0].isalpha() and s[1].isalpha():
                for i in range(len(s)):
                    if s[i].isdigit():
                        if s[i:].isdigit() and s[i] != '0':
                            return True
                        else:
                            return False
                return True
            else:
                return False
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()