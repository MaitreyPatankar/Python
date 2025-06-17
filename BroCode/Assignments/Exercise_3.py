# Circumference and area of a circle

import math

radius = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius
area = math.pi * pow(radius, 2)

print(f"The circumference is: {round(circumference, 3)} 5cm")
print(f"The area is: {round(area, 3)} cm^2")

# round(number_to_be_rounded, number_of_digits_to_round)