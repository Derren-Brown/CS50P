def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        s = input("Date: ")
        if '/' not in s:
            try:
                time = s.split()
                for i in range(12):
                    if months[i] == time[0]:
                        month = i + 1
                        break
                day = int(time[1][:-1])
                year = int(time[2])
            except ValueError:
                pass
            else:
                if (0 < month < 13 and 0 < day < 32):
                    print(f"{year:04}-{month:02}-{day:02}")
                    break
        else:
            try:
                month, day, year = s.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
            except ValueError:
                pass
            else:
                if (0 < month < 13 and 0 < day < 32):
                    print(f"{year:04}-{month:02}-{day:02}")
                    break


if __name__ == "__main__":
    main()