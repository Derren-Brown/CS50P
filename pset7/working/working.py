import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    s = s.strip()
    if matches := re.search(r"([0-9]+ [A|P]M) to ([0-9]+ [A|P]M)", s):
        s1 = matches.group(1)
        s2 = matches.group(2)
        if s1[0] == "0" and s1[1] != " ":
            return ValueError(1)
        if s2[0] == "0" and s2[1] != " ":
            return ValueError(1)
        try:
            if s1.endswith("PM"):
                hour1 = int(s1.removesuffix(" PM")) + 12
            else:
                hour1 = int(s1.removesuffix(" AM"))
            if s2.endswith("PM"):
                hour2 = int(s2.removesuffix(" PM")) + 12
            else:
                hour2 = int(s2.removesuffix(" AM"))
        except ValueError:
            raise ValueError(1)
        minute1 = minute2 = 0
    elif matches := re.search(r"([0-9]+:[0-9]+ [A|P]M) to ([0-9]+:[0-9]+ [A|P]M)", s):
        s1 = matches.group(1)
        s2 = matches.group(2)
        if s1[0] == "0" and s1[1] != " ":
            return ValueError(1)
        if s2[0] == "0" and s2[1] != " ":
            return ValueError(1)
        try:
            if s1.endswith("PM"):
                s1 = s1.removesuffix(" PM")
                hour1, minute1 = s1.split(":")
                hour1 = int(hour1) + 12
                minute1 = int(minute1)
            else:
                s1 = s1.removesuffix(" AM")
                hour1, minute1 = s1.split(":")
                hour1 = int(hour1)
                minute1 = int(minute1)
            if s2.endswith("PM"):
                s2 = s2.removesuffix(" PM")
                hour2, minute2 = s2.split(":")
                hour2 = int(hour2) + 12
                minute2 = int(minute2)
            else:
                s2 = s2.removesuffix(" AM")
                hour2, minute2 = s2.split(":")
                hour2 = int(hour2)
                minute2 = int(minute2)
        except ValueError:
            raise ValueError(1)
    else:
        raise ValueError(1)
    if hour1 == 12:
        hour1 = 0
    elif hour1 == 24:
        hour1 = 12
    if hour2 == 12:
        hour2 = 0
    elif hour2 == 24:
        hour2 = 12
    if (
        0 <= hour1 <= 24
        and 0 <= hour2 <= 24
        and 0 <= minute1 < 60
        and 0 <= minute2 < 60
    ):
        return f"{hour1:02}:{minute1:02} to {hour2:02}:{minute2:02}"
    else:
        raise ValueError(1)


if __name__ == "__main__":
    main()
