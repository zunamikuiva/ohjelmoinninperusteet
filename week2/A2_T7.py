# A2_T7 Fahrenheit to Celcius  

print("Program starting.")
fahr = float(input("Insert fahrenheits: "))
celc = (fahr - 32) / 1.8
celc = round(celc, 1)
print(f"{fahr}°F is {celc}°C")
print("Program ending.")
