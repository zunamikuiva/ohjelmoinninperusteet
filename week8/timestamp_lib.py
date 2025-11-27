from datetime import datetime

MONTHS = (
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
)

WEEKDAYS = (
    "Monday","Tuesday","Wednesday","Thursday",
    "Friday","Saturday","Sunday"
)


def readTimestamps(PFilename: str, PTimestamps: list[datetime]) -> None:
    file = open(PFilename, "r")

    row = file.readline()
    while row != "":
        row = row.strip()
        if row != "":
            timestamp = datetime.strptime(row, "%Y-%m-%d %H:%M")
            PTimestamps.append(timestamp)
        row = file.readline()

    file.close()


def calculateYears(PYear: int, PTimestamps: list[datetime]) -> int:
    count = 0
    for ts in PTimestamps:
        if ts.year == PYear:
            count += 1
    return count


def calculateMonths(PMonth: str, PTimestamps: list[datetime]) -> int:
    monthIndex = MONTHS.index(PMonth) + 1
    count = 0

    for ts in PTimestamps:
        if ts.month == monthIndex:
            count += 1
    return count


def calculateWeekdays(PWeekday: str, PTimestamps: list[datetime]) -> int:
    weekdayIndex = WEEKDAYS.index(PWeekday)
    count = 0

    for ts in PTimestamps:
        if ts.weekday() == weekdayIndex:
            count += 1
    return count
