# Hypotenuse of a right angled triangle
import math

x = float(input("Enter a side: "))
y = float(input("Enter another side: "))

z = math.sqrt(pow(x, 2) + pow(y, 2))

print(f"The length of hypotenuse is: {z} cm")

# not importing math will result in run time error