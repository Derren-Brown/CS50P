import sys
import csv


def main():
    if len(sys.argv) < 3:
        print("Too few arguments")
        sys.exit(1)
    if len(sys.argv) > 3:
        print("Too many arguments")
        sys.exit(1)
    fieldnames = ["first", "last", "house"]
    students = []
    try:
        with open(sys.argv[1], "r") as f1:
            reader = csv.DictReader(f1)
            for row in reader:
                name = row["name"]
                house = row["house"]
                last, first = name.split(", ")
                students.append({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        print(f"Coundn't read {sys.argv[1]}")
        sys.exit(1)
    with open(sys.argv[2], "w") as f2:
        writer = csv.DictWriter(f2, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(
                {
                    "first": student["first"],
                    "last": student["last"],
                    "house": student["house"],
                }
            )


if __name__ == "__main__":
    main()
