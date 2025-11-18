# A7_T5 Analyse electricity usage


WEEKDAYS = (
    "Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturnday", "Sunday"
)

TIMESTAMP = tuple[str, int, float, float]

DAY_USAGE = dict[str, float]


def readTimestamps(PFilename: str, PTimestamps: list[TIMESTAMP]) -> None:
    print(f'Reading file "{PFilename}".')

    PTimestamps.clear()

    with open(PFilename, "r", encoding="utf-8") as fh:
        header = fh.readline()

        for row in fh:
            row = row.strip()

            if row == "":
                continue

            parts = row.split(";")
            if len(parts) != 4:
                continue

            weekday = parts[0]
            hour = int(parts[1])
            consumption = float(parts[2])
            price = float(parts[3])

            PTimestamps.append((weekday, hour, consumption, price))

    return None


def analyseUsage(PTimestamps: list[TIMESTAMP], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    PResults.clear()

    helper: dict[str, DAY_USAGE] = {}

    for day in WEEKDAYS:
        helper[day] = {"usage": 0.0, "cost": 0.0}

    for ts in PTimestamps:
        weekday, _, consumption, price = ts
        if weekday in helper:
            helper[weekday]["usage"] += consumption
            helper[weekday]["cost"] += consumption * price

    PResults.append("### Electricity consumption summary ###")
    for day in WEEKDAYS:
        usage = helper[day]["usage"]
        cost = helper[day]["cost"]
        PResults.append(f" - {day} usage {usage:.2f} kWh, cost {cost:.2f} €")
    PResults.append("### Electricity consumption summary ###")

    return None


def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    for line in PResults:
        print(line)
    return None


def main() -> None:
    print("Program starting.")

    timestamps: list[TIMESTAMP] = []
    results: list[str] = []

    filename = input("Insert filename: ")

    readTimestamps(filename, timestamps)
    analyseUsage(timestamps, results)
    displayResults(results)

    timestamps.clear()
    results.clear()

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
