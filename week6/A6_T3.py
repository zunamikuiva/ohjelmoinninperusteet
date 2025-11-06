#A6_T3 Copy text file 


def main():
    print("Program starting.")
    print("This program can copy a file.")

    source = input("Inser source filename: ")
    destination = input("Insert destination filename: ")

    print(f"Reading file {source} content.")
    readFile = open(source, "r", encoding="utf-8")
    lines = []
    while True:
        line = readFile.readline()
        if len(line) == 0:
            break
        lines.append(line)
    readFile.close()
    print("File content ready in memory.")

    print(f"Writing content into file {destination}")
    writeFile = open(destination, "w", encoding="utf-8")
    for line in lines:
        writeFile.write(line)
    writeFile.close()

    print("Copying operation complete.")
    print("Program ending.")

main()