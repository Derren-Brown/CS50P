def main():
    names = []
    while True:
        try:
            s = input("Name: ")
        except EOFError:
            break
        names.append(s)
    print(f"Adieu, adieu, to {names[0]}", end="")
    if len(names) > 2:
        for i in range(1, len(names) - 1):
            print(f", {names[i]}", end="")
        print(f", and {names[len(names) - 1]}")
    if len(names) == 2:
        print(f" and {names[len(names) - 1]}")



if __name__ == "__main__":
    main()
