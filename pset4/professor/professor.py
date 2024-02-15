from random import randint


def main():
    cnt = 0
    level = get_level()
    for _ in range(10):
        cnt1 = 0
        x = generate_integer(level)
        y = generate_integer(level)
        while cnt1 < 3:
            try:
                res = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
            else:
                if res != x + y:
                    print("EEE")
                else:
                    break
            cnt1 += 1
        if cnt1 == 3:
            print(f"{x} + {y} = {x+y}")
        else:
            cnt += 1
    print(f"Score: {cnt}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 0 < n < 4:
                return n
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return randint(0, 9)
    elif level == 2:
        return randint(10, 99)
    else:
        return randint(100, 999)

if __name__ == "__main__":
    main()