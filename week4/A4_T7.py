#A4_T7 Multiplicative persistency 


print("Program starting.\n")
print("Check multiplicative persistence.")
num = int(input("Insert an integer: "))

steps = 0

while num >= 10:
    temp = num
    result = 1
    print(end="")

    first = True
    while temp > 0:
        digit = temp % 10
        temp = temp // 10
        result = result * digit

        if not first:
            print(" *", end="")
        print(" " + str(digit), end="")
        first = False

    print(" =", result)
    num = result
    steps += 1

print("No more steps.\n")
print("This program took", steps, "step(s)\n")
print("Program ending.")
