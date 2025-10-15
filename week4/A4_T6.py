# A4_T6 Collatz Conjecture

print("Program starting.")
num = int(input("Insert a positive integer: "))

steps = 0
print(num, end="")

while num != 1:
    if num % 2 == 0:
        num = num // 2
    else:
        num = num * 3 + 1
    print(" ->", num, end="")
    steps += 1

print(f"\nSequence had {steps} total steps.\n")
print("Program ending.")
