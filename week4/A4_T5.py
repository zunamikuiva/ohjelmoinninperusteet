#A4_T5 Break and continue 


print("Program starting.\n")

start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspection = int(input("Insert inspection point: "))

error = False

if start >= stop:
    print("\nStarting point value must be less than the stopping point value.")
    error = True

if inspection < start or inspection > stop:
    print("Inspection value must be within the range of start and stop.")
    error = True

if not error:
    print("\nFirst loop - inspection with break:")
    for i in range(start, stop):
        if i == inspection:
            break
        else:
            print(i, end=' ')

    print("\nSecond loop - inspection with continue:")
    for i in range(start, stop):
        if i == inspection:
            continue
        else:
            if(i == stop):
                print(i)
            print(i, end=' ')

print("\nProgram ending.")