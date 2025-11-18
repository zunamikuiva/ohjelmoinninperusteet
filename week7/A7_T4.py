# A7_T4 Structure timestamp data


DELIMITER = ";"


class TIMESTAMP:
    def __init__(self):
        self.weekday: str = ""
        self.hour: str = ""
        self.consumption: float = 0.0
        self.price: float = 0.0


def readTimestamps(filename: str, timestamps: list[TIMESTAMP]) -> None:
    print(f'Reading file "{filename}".')

    timestamps.clear()

    try:
        with open(filename, "r") as f:
            first = True
            for line in f:
                if first:
                    first = False
                    continue

                row = line.rstrip()

                if row.strip() == "":
                    continue

                columns = row.split(DELIMITER)

                ts = TIMESTAMP()
                ts.weekday = columns[0]
                ts.hour = columns[1]
                ts.consumption = float(columns[2])
                ts.price = float(columns[3])

                timestamps.append(ts)

                columns.clear()

    except FileNotFoundError:
        print(f'File "{filename}" not found.')

    return None


def displayTimestamps(timestamps: list[TIMESTAMP]) -> None:
    print("Electricity usage:")

    for ts in timestamps:
        total = ts.consumption * ts.price
        print(f" - {ts.weekday} {ts.hour}, price {ts.price:.2f}, "
              f"consumption {ts.consumption:.2f} kWh, total {total:.2f} €")

    return None


def main() -> None:
    print("Program starting.")

    timestamps: list[TIMESTAMP] = []

    filename = input("Insert filename: ")

    readTimestamps(filename, timestamps)
    displayTimestamps(timestamps)

    timestamps.clear()

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
