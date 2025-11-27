########################################################
# Task A9_T2 Exit codes
# Developer Nina Hinkkanen
# Date 2025-11-27
########################################################

import sys

def main() -> None:
    print("Program starting.\n")
    code_str = input("Insert exit code(0-255): ")
    try:
        code = int(code_str)
        if 0 <= code <= 255:
            print("Clean exit")
            sys.exit(code)
        else:
            print("Error! Exit code must be between 0 and 255.")
            sys.exit(1)
    except ValueError:
        print(f"Error! '{code_str}' is not a valid integer.")
        sys.exit(1)

if __name__ == "__main__":
    main()
