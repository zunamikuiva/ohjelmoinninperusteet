#A3_T5 Temperature converter(TEST TASK)  


print("Program starting.\n")

print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")

choise = int(input("Your choise: "))

if choise == 1:
    celsius = float(input("Insert the amount of Celsius: "))
    fahrenheit = celsius * 1.8 + 32
    print(f"{celsius:.1f} °C equals to {fahrenheit:.1f} °F")
elif choise == 2:
    fahrenheit = float(input("Insert the amount of Fahrenheit: "))
    celsius = (fahrenheit - 32) / 1.8
    print(f"{fahrenheit:.1f} °F equals to {celsius:.1f} °C")
elif choise == 0:
    print("Exiting...")
else:
    print("Unokwn option.")

print("\nProgram ending.")

