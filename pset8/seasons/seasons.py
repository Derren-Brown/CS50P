import datetime
import sys
import inflect


def main():
    p_date = convert(input("Date of birth: "))
    today = datetime.date.today()
    date = today.__sub__(p_date)
    minutes = round(
        date.days * 24 * 60 + date.seconds / 60 + date.microseconds / 1000 / 60
    )
    p = inflect.engine()
    s = p.number_to_words(str(minutes), andword="")
    print(f"{s} minutes".capitalize())


def convert(s):
    try:
        return datetime.date.fromisoformat(s)
    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
