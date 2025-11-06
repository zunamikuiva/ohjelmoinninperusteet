#A6_T1 Read text file 


print("Program starting.")
print("This program can read a file.")


fileName = input("Insert filename: ")
file = open(fileName, "r", encoding="utf-8")

print(f"### START {fileName} ###")

while True:
    line = file.readline()
    if len(line) == 0:
        break
    print(line, end="")

print(f"\n### END {fileName} ###")
print("Program ending.")

file.close()
