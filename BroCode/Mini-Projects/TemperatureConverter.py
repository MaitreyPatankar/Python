temp = float(input("Enter the temperature: "))
unit = input("Is this temperature in Celcius or Fahrenheit (C/F): ")

if unit == "C":
  temp = round((((9 * temp) / 5) + 32), 3)
  print(f"The temperature in Fahrenheit is: {temp}°F")

elif unit == "F":
  temp = round(((temp - 32) * 5) / 9, 3)
  print(f"The temperature in Celcius is: {temp}°C")

else:
  print(f"{unit} is an invalid unit of measurement")


# Alt + 0176 => °