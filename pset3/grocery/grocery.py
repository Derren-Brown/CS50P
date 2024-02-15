def main():
    grocery = {}
    while True:
        try:
            item = input()
        except EOFError:
            break
        item = item.upper()
        if item not in grocery:
            grocery[item] = 1
        else:
            grocery[item] += 1
    sorted_keys = sorted(grocery.keys())
    for key in sorted_keys:
        print(f"{grocery[key]} {key}")

if __name__ == "__main__":
    main()