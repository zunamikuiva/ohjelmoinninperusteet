# A8_T3 Number files


def showOptions() -> None:
    print("Options:")
    print("1 - Read values")
    print("2 - Amount of values")
    print("3 - Calculate sum of values")
    print("4 - Calculate average of values")
    print("0 - Exit")


def readValues(filename: str) -> list[float]:
    values = []
    file = open(filename, "r")

    row = file.readline()
    while row != "":
        row = row.strip()
        if row != "":
            values.append(float(row))
        row = file.readline()

    file.close()
    return values


def calculateSum(values: list[float]) -> float:
    return round(sum(values), 1)


def calculateAverage(values: list[float]) -> float:
    if len(values) == 0:
        return 0.0
    return round(sum(values) / len(values), 1)


def main() -> None:
    print("Program starting.")

    values = []
    choice = -1

    while choice != 0:
        showOptions()
        choice = int(input("Your choice: "))

        if choice == 1:
            filename = input("Insert filename: ")
            values = readValues(filename)
            print()

        elif choice == 2:
            print(f"Amount of values {len(values)}\n")

        elif choice == 3:
            total = calculateSum(values)
            print(f"Sum of values {total}\n")

        elif choice == 4:
            average = calculateAverage(values)
            print(f"Average of values {average}\n")

        elif choice == 0:
            print("Exiting program.")

    print()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
