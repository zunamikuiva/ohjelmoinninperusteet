# A7_T1 Positive integer collector


def collectIntegers():
    numbers = []

    print("Collect positive integers.")

    while True:
        integer = int(input("Insert positive integer (negative stops): "))
        if integer < 0:
            print("Stopped collecting positive integers.")
            break
        numbers.append(integer)

    return numbers

def main():
    print("Program starting.")
    numbers = collectIntegers()

    if len(numbers) == 0:
        print("No integers to display.")
    else:
        print(f"Displaying {len(numbers)} integers:")
        for index, value in enumerate(numbers):
            ordinal = index + 1
            print(f"- Index {index} => Ordinal {ordinal} => Integer {value}")
    
    print("Program ending.")

main()