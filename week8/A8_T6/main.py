from drawLib import drawCircle, drawSquare, saveSvg, Drawing


def main() -> None:
    Dwg = Drawing()
    print("Program starting.")
    while True:
        showOptions()
        choice = askChoice()

        match choice:
            case 1:
                print("Insert square")
                left = askValue1("Left edge position")
                top = askValue1("Top edge position")
                side = askValue1("Side length")
                color = askValue1("Fill color")
                stroke = askValue1("Stroke color")

                drawSquare(Dwg, int(left), int(top), int(side), color, stroke)

            case 2:
                print("Insert circle")
                cx = askValue1("Center x position")
                cy = askValue1("Center y position")
                radius = askValue1("Radius")
                color = askValue1("Fill color")
                stroke = askValue1("Stroke color")

                drawCircle(Dwg, int(cx), int(cy), int(radius), color, stroke)

            case 3:
                filename = askValue2("Insert filename")
                print(f'Saving file to "{filename}"')
                confirm = input("Proceed (y/n)?: ")
                if confirm.lower() == "y":
                    saveSvg(Dwg, filename)
                    print("Vector saved successfully!")

            case 0:
                print("Exiting program.\n")
                break
        print()

    print("Program ending.")


def showOptions() -> None:
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Save svg")
    print("0 - Exit")


def askChoice() -> int:
    return int(input("Your choice: "))


def askValue1(PPrompt: str) -> str:
    return input(f"- {PPrompt}: ")


def askValue2(PPrompt: str) -> str:
    return input(f"{PPrompt}: ")


if __name__ == "__main__":
    main()
