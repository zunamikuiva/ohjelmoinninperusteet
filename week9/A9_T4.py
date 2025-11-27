########################################################
# Task A9_T4 Reasonable celsius
# Developer Nina Hinkkanen
# Date 2025-11-27
########################################################

TEMP_MIN = -273.15
TEMP_MAX = 10000

def collectCelsius() -> float:
    value = input("Insert Celsius: ")
    try:
        celsius = float(value)
    except ValueError:
        raise ValueError(f"could not convert string to float: '{value}'")
    if not (TEMP_MIN <= celsius <= TEMP_MAX):
        raise Exception(f"{celsius} temperature out of range.")
    return celsius

def main() -> None:
    print("Program starting.\n")
    try:
        celsius = collectCelsius()
        print(f"You inserted {celsius} °C")
    except Exception as e:
        print(f"Error! {e}")
    print("Program ending.")

if __name__ == "__main__":
    main()
