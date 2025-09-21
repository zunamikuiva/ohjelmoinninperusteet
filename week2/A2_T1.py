#A2_T1 Basic program structure 


print("Program starting.")

# Kysytään käyttäjän nimeä
name = input("What is your name: ")

# Pyydetään numerot
num1 = float(input("Enter a floating point number: "))
num2 = float(input("Enter second floating point number: "))
print(f"{name} you gave numbers {num1} and {num2}")

# Lasketaan luvut
sum = num1 * num2
print(f"Multiplying first and second number will result in product {sum}")
print("Program ending.")