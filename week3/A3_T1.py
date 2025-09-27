#A3_T1 If-statements  


print("Program starting.")
print("Insert two integers.")
first = int(input("Insert first integer: "))
sec = int(input("Insert second integer: "))
sum = first + sec
print("Comparing inserted integer.")
if first > sec:
    print("First integer is greater.\n")
elif first < sec:
    print("Second integer is greater.\n")
else:
    print("Integers are the same.\n")

print("Adding integers together")
print(f"{first} + {sec} = {sum}\n")

print("Checking the parity of the sum...")
if sum % 2 == 0:
    print("Sum is even")
else:
    print("Sum is odd.")
print("Program ending.")
