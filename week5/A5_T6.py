#A5_T6 Tally counter 


def showOptions():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")

def askChoice():
    choice = input("Your choise: ")
    if not choice.isnumeric():
        return -1
    return int(choice)

def main():
    print("Program starting.")
    count = 0
    choice = ""
    while choice != 0:
        showOptions()
        choice = askChoice()
        if choice == 1:
            print(f"Current count - {count}")
        elif choice == 2:
            count += 1
            print("Count increased!")
        elif choice == 3:
            count = 0
            print("Cleared count!")
        elif choice == 0:
            print("Exiting program.")
        else:
            print("Unknown option!")

main()