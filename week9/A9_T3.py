########################################################
# Task A9_T3 File exists
# Developer Nina Hinkkanen
# Date 2025-11-27
########################################################

import sys
import os

def main() -> None:
    print("Program starting.\n")
    filename = input("Insert filename: ")
    if not os.path.isfile(filename):
        print(f"Error! File '{filename}' does not exist.")
        sys.exit(1)

    print(f"## {filename} ##")
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())
    print(f"## {filename} ##")
    print("Program ending.")

if __name__ == "__main__":
    main()
