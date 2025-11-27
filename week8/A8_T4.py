#A8_T4 Years, Months and Days


from datetime import datetime
import timestamp_lib


def showOptions() -> None:
    print("Options:")
    print("1 - Calculate amount of timestamps during year")
    print("2 - Calculate amount of timestamps during month")
    print("3 - Calculate amount of timestamps during weekday")
    print("0 - Exit")


def main() -> None:
    print("Program starting.")

    timestamps: list[datetime] = []

    filename = input("Insert filename: ")
    timestamp_lib.readTimestamps(filename, timestamps)

    choice = -1

    while choice != 0:
        showOptions()
        choice = int(input("Your choice: "))

        if choice == 1:
            year = int(input("Insert year: "))
            amount = timestamp_lib.calculateYears(year, timestamps)
            print(f"Amount of timestamps during year '{year}' is {amount}\n")

        elif choice == 2:
            month = input("Insert month: ")
            amount = timestamp_lib.calculateMonths(month, timestamps)
            print(f"Amount of timestamps during month '{month}' is {amount}\n")

        elif choice == 3:
            weekday = input("Insert weekday: ")
            amount = timestamp_lib.calculateWeekdays(weekday, timestamps)
            print(f"Amount of timestamps during weekday '{weekday}' is {amount}\n")

        elif choice == 0:
            print("Exiting program.")

    print()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
