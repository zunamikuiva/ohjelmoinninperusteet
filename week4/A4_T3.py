#A4_T3 While-loop 


print("Program starting.\n")

val1 = int(input("Insert starting value: "))
val2 = int(input("Insert stopping value: "))

print("\nStarting while-loop:")
i = val1
while i <= val2:
    print(i, end=" ")
    i += 1

print("\nProgram ending.")
