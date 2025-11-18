# A7_T2 Analyse separated values


def commaIntegers():
    raw_input = input("Insert comma separated integers: ")

    parts = raw_input.split(",")
    numbers = []
    errors = []

    for p in parts:
        p = p.strip()
        try:
            number = int(p)
            numbers.append(number)
        except ValueError:
            errors.append(p)

    for e in errors:
        print(f"Invalid value detected: {e}")

    return numbers

def main():
    print("Program starting.")
    numbers = commaIntegers()

    if len(numbers) == 0:
        print("No valid integers to analyze.")
        print("Program ending.")
        return
    
    total = sum(numbers)
    count = len(numbers)

    if total % 2 == 0:
        parity = "even"
    else:
        parity = "odd"

    print(f"There are {count} integers in the list.")
    print(f"Sum of the integers is {total} and it's {parity}.")

    print("Program ending.")

main()