#A2_T5 String length and slicing 


print("Program starting.\n")

word = input("Insert a closed compound word: ")
reverse = word[::-1]

print(f"The word you inserted is '{word}' and in reverse it is '{reverse}'.")

length = (len(word))
print(f"The inserter word length is {length}")

last = word[-1]
print(f"Last character is '{last}'\n")

print("Take substring from the inserted word by inserting...")
first = int(input("1) Starting point: "))
second = int(input("2) Ending point: "))
third = int(input("3) Step size: "))
complete= word[first:second:third]

print(f"\nThe word '{word}' sliced to the defined substring is '{complete}'.")
print("Program ending.")