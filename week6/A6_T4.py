# A6_T4 String analytics 

def main():
    print("Program starting.")
    print("This program analyses a list of names from a file.")

    filename = input("Insert filename to read: ")
    print(f'Reading names from "{filename}".')

    file = open(filename, "r", encoding="utf-8")
    names = []

    while True:
        line = file.readline()
        if len(line) == 0:
            break
        line = line.strip()
        if line == "":
            continue
        parts = line.split(";")
        for name in parts:
            name = name.strip()
            if name != "":
                names.append(name)
    file.close()

    print("Analysing names...")

    count = len(names)
    if count > 0:
        lengths = [len(n) for n in names]
        shortest = min(lengths)
        longest = max(lengths)
        average = sum(lengths) / count
    else:
        shortest = longest = average = 0

    print("Analysis complete!")
    print("#### REPORT BEGIN ####")
    print("Name count - {}".format(count))
    print("Shortest name - {} chars".format(shortest))
    print("Longest name - {} chars".format(longest))
    print("Average name - {:.2f} chars".format(average))
    print("#### REPORT END ####")
    print("Program ending.")

main()
