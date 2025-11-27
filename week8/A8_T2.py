#A8_T2 Calculator


import calculator


def showOptions() -> None:
    print("Options:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")


def askChoice() -> int:
    return int(input("Your choice: "))


def askValue(PPrompt: str) -> float:
    return float(input(PPrompt))


def main() -> None:
    print("Program starting.")

    choice = -1

    while choice != 0:
        showOptions()
        choice = askChoice()

        if choice == 1:
            value1 = askValue("Insert first addend value: ")
            value2 = askValue("Insert second addend value: ")
            result = calculator.add(value1, value2)
            print(f"{value1} + {value2} = {result}\n")

        elif choice == 2:
            value1 = askValue("Insert minuend value: ")
            value2 = askValue("Insert subtrahend value: ")
            result = calculator.subtract(value1, value2)
            print(f"{value1} - {value2} = {result}\n")

        elif choice == 3:
            value1 = askValue("Insert multiplicant value: ")
            value2 = askValue("Insert multiplier value: ")
            result = calculator.multiply(value1, value2)
            print(f"{value1} * {value2} = {result}\n")

        elif choice == 4:
            value1 = askValue("Insert dividend value: ")
            value2 = askValue("Insert divisor value: ")
            result = calculator.divide(value1, value2)
            print(f"{value1} / {value2} = {result}\n")

        elif choice == 0:
            print("Exiting program.")

    print()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
