#A3_T3 Menu program  


print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")
name = input("Before the menu, please insert your name: ")

print("\n Options: ")
print("1 - Print welcome message")
print("0 - Exit")

choise = int(input("Your choise: "))

if choise == 1:
    print(f"Welcome {name}!")
elif choise == 0:
    print("Exiting...")
else:
    print("Unokwn option.")
print("\nProgram ending.")