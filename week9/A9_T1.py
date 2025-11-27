########################################################
# Task A9_T1 Faulty user input
# Developer Nina Hinkkanen
# Date 2025-11-27
########################################################

def main() -> None:
    print("Program starting.\n")
    total = 0.0

    while True:
        value = input("Insert a floating-point value (0 to stop): ")
        if value == "0":
            break
        try:
            fvalue = float(value)
            total += fvalue
        except ValueError:
            print(f"Error! '{value}' couldn't be converted to float.")

    print(f"\nFinal sum is {total:.2f}")
    print("Program ending.")

if __name__ == "__main__":
    main()
