#A5_T2 Pass argument 


def frameWord(PWord):
    stars = "*" * (len(PWord) + 4)
    print(stars)
    print(f"* {PWord} *")
    print(stars)
    return None

def main():
    print("Program starting.")
    word = input("Insert word: ")
    print()
    frameWord(word)
    print("\nProgram ending.")
    return None

main()
    
    