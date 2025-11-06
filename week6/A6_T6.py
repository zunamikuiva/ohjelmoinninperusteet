# A6_T6 Cipher messages (TEST TASK)


LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def shiftCharacter(ch, alphabet):
    index = alphabet.find(ch)
    if index == -1:
        return ch
    return alphabet[(index + 13) % 26]


def rot13(text):
    result = ""
    for ch in text:
        if ch in LOWER_ALPHABETS:
            result += shiftCharacter(ch, LOWER_ALPHABETS)
        elif ch in UPPER_ALPHABETS:
            result += shiftCharacter(ch, UPPER_ALPHABETS)
        else:
            result += ch
    return result


def writeFile(fileName, content):
    fileHandler = open(fileName, "w", encoding="UTF-8")
    fileHandler.write(content)
    fileHandler.close()
    return None


def main() -> None:
    print("Program starting.")
    print()
    print("Collecting plain text rows for ciphering.")

    rows = []
    row = input("Insert row(empty stops): ")
    while row != "":
        rows.append(row)
        row = input("Insert row(empty stops): ")

    cipheredText = ""
    for r in rows:
        cipheredText += rot13(r) + "\n"

    print()
    print("#### Ciphered text ####")
    print(cipheredText.strip())

    print()
    print("#### Ciphered text ####")
    fileName = input("Insert filename to save: ")
    if fileName != "":
        writeFile(fileName, cipheredText)
        print("Ciphered text saved!")

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()