temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit: ")
if unit == "Celsius":
    print((temperature * 9/5) + 32, "Fahrenheit")
elif unit == "Fahrenheit":
    print((temperature-32)* 5/9, "Celsius")
else:
    print("Invalid unit entered")
