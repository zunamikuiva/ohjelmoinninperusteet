#A5_T3 Ask name 


def askName():
    username = input("Insert name: ")
    return username

def greetUser(PName):
    print(f"Hello {PName}!")
    return None

def main():
    print("Program starting.")
    username = askName()
    greetUser(username)
    return None

main()