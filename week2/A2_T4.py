#A2_T4 Average and rounding 


print("Program starting.")
print("Estimate how many minutes you spent on programming...\n")

T1 = int(input("A1_T1: "))
T2 = int(input("A1_T2: "))
T3 = int(input("A1_T3: "))
T4 = int(input("A1_T4: "))
T5 = int(input("A1_T5: "))
T6 = int(input("A1_T6: "))
T7 = int(input("A1_T7: "))

total = T1 + T2 + T3 + T4 + T5 + T6 + T7
average = float(total / 7)

print(f"\nIn total you spent {total} minutes on programming.")
print(f"Average per task was {round(average,2)} min and same rounded to the nearest integer {round(average)} min.")
print("\nProgram ending.")