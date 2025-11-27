from drawLib import drawCircle, drawSquare, drawHexagon, saveSvg, Drawing

def main() -> None:
    Dwg = Drawing()
    print("Program starting.")
    
    while True:
        showOptions()
        choice = askChoice()
        match choice:
            case 1:
                print('Insert square')
                left = float(askValue1("Left edge position"))
                top = float(askValue1("Top edge position"))
                side = float(askValue1("Side length"))
                fill = askValue1("Fill color")
                stroke = askValue1("Stroke color")
                drawSquare(Dwg, left, top, side, fill, stroke)
            case 2:
                print('Insert circle')
                cx = float(askValue1("Center X"))
                cy = float(askValue1("Center Y"))
                radius = float(askValue1("Radius"))
                fill = askValue1("Fill color")
                stroke = askValue1("Stroke color")
                drawCircle(Dwg, cx, cy, radius, fill, stroke)
            case 3:
                print('Insert hexagon details:')
                cx = float(askValue1("Middle point X"))
                cy = float(askValue1("Middle point Y"))
                apothem = float(askValue1("Apothem length"))
                fill = askValue1("Insert fill")
                stroke = askValue1("Insert stroke")
                drawHexagon(Dwg, cx, cy, apothem, fill, stroke)
            case 4:
                filename = askValue1("filename")
                confirm = askValue1(f'Saving file to "{filename}"\nProceed (y/n)?')
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
    print("3 - Draw hexagon")
    print("4 - Save svg")
    print("0 - Exit")

def askChoice() -> int:
    return int(input("Your choice: "))

def askValue1(PPrompt: str) -> str:
    return input(f"- {PPrompt}: ")

if __name__ == "__main__":
    main()
