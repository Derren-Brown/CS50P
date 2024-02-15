def main():
    word = input("Input: ")
    res = shorten(word)
    print(res)


def shorten(s):
    vowels = ["A", "O", "U", "I", "E"]
    res = ""
    for c in s:
        if c.upper() in vowels:
            pass
        else:
            res += c
    return res


if __name__ == "__main__":
    main()
