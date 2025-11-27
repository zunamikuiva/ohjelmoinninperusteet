# A8_T1 Pause


import time


def showOptions() -> None:
    print("Options:")
    print("1 - Set pause duration")
    print("2 - Activate pause")
    print("0 - Exit")


def main() -> None:
    print("Program starting.")

    pauseDuration = 1.0
    choice = -1

    while choice != 0:
        showOptions()
        choice = int(input("Your choice: "))

        if choice == 1:
            pauseDuration = float(input("Insert pause duration (s): "))
            print()

        elif choice == 2:
            print(f"Pausing for {pauseDuration} seconds.")
            time.sleep(pauseDuration)
            print("Unpaused.\n")

        elif choice == 0:
            print("Exiting program.")

    print()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()