# A7_T3 Analyse timestamps

WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday")


def readFile(PFilename: str, PRows: list[str]) -> None:
    print(f'Reading file "{PFilename}".')

    PRows.clear()

    try:
        with open(PFilename, "r") as f:
            first = True
            for line in f:
                if first:
                    first = False
                    continue

                line = line.rstrip("\n")

                if line.strip() == "":
                    continue

                PRows.append(line)
    except FileNotFoundError:
        print(f'File "{PFilename}" not found.')
    return None


def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")

    PResults.clear()

    WeekdayTimestampAmount = [0, 0, 0, 0, 0, 0, 0]

    for row in PRows:
        for j in range(len(WEEKDAYS)):
            if row.startswith(WEEKDAYS[j]):
                WeekdayTimestampAmount[j] += 1

    for i in range(len(WEEKDAYS)):
        dayName = WEEKDAYS[i]
        amount = WeekdayTimestampAmount[i]
        PResults.append(f" - {dayName} {amount} stamps")

    return None


def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    print("### Timestamp analysis ###")
    for r in PResults:
        print(r)
    print("### Timestamp analysis ###")
    return None


def main() -> None:
    print("Program starting.")

    rows: list[str] = []
    results: list[str] = []

    filename = input("Insert filename: ")

    readFile(filename, rows)
    analyseTimestamps(rows, results)
    displayResults(results)

    rows.clear()
    results.clear()

    print("Program ending.")
    return None


main()
