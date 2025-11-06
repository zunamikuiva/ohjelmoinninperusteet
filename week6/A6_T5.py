# A6_T5 Number analytics

SEPARATOR = ";"


def readValues(filename: str) -> str:
    """Reads integer values from the given file and returns them as a semicolon-separated string."""
    file = open(filename, "r", encoding="utf-8")
    values = ""
    while True:
        line = file.readline()
        if len(line) == 0:
            break
        line = line.strip()
        if len(values) > 0:
            values += SEPARATOR
        values += line
    file.close()
    return values


def analyseValues(values: str) -> str:
    """Takes semicolon-separated numbers as input and returns analysis results as a single string."""
    parts = values.split(SEPARATOR)
    numbers = [int(x) for x in parts]

    count = len(numbers)
    total = sum(numbers)
    greatest = max(numbers)
    average = total / count

    
    result = (
        "Count;Sum;Greatest;Average\n"
        f"{count}{SEPARATOR}{total}{SEPARATOR}{greatest}{SEPARATOR}{average:.2f}\n"
    )
    return result


def displayResults(filename: str, results: str):
    """Prints the results in the required CSV format."""
    print(f'File "{filename}" results:')
    print(results, end="")


def main():
    print("Program starting.")
    filename = input("Insert filename: ")

    print("#### Number analysis - START ####")

    values = readValues(filename)
    results = analyseValues(values)
    displayResults(filename, results)

    print("\n#### Number analysis - END ####")
    print("Program ending.")


if __name__ == "__main__":
    main()
