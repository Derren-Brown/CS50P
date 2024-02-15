def main():
    s = input("Input: ")
    for c in s:
        C = c.upper()
        if C == 'A' or C == 'E' or C == 'I' or C == 'O' or C == 'U':
            pass
        else:
            print(c, end='')
    print()

if __name__ == "__main__":
    main()