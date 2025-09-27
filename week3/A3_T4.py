#A3_T4 More menu options  


print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")
name = input("Before the menu, please insert your name: ")

print("\n Options: ")
print("1 - Print welcome message")
print("2 - Print the name backwards")
print("3 - Print the first character")
print("4 - Print the amount of characters in the name")
print("0 - Exit")

choise = int(input("Your choise: "))

if choise == 1:
    print(f"Welcome {name}!")
elif choise == 0:
    print("Exiting...")
elif choise == 2:
    print(f"Your name backwards is \"{name[::-1]}\"")
elif choise == 3:
    print(f"The first character in name \"{name}\" is \"{name[0]}\"")
elif choise == 4:
    print(f"There are {len(name)} characters in the name \"{name}\"")
else:
    print("Unokwn option.")
print("\nProgram ending.")