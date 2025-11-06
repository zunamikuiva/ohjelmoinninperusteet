#A6_T2 Write text file 


print("Program starting.")

firstName = input("Insert first name: ")
lastName = input("Insert last name: ")
fileName = input("Insert file name: ")

file = open(fileName, "w", encoding="utf-8")

file.write(firstName + "\n")
file.write(lastName + "\n")
file.write("\n")

file.close()

print("Program ending.")