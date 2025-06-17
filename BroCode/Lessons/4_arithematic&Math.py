import math

friends = 0
# Addition
# friends = friends + 1
friends += 1 # Augmented assignment operator

# Subtraction
friends -= 2

# Multiplication
friends *= 3

# Division
friends /= 2

# Exponents
#friends = friends ** 2
friends **= 2

# Modulus
remainder = friends % 3

print(friends)

# Math related functions
x = 3.14
y = -4
z = 5

result = round(x) # nearest whole integer
result = abs(y) # distance from 0
result = pow(y,3) # pow(base, exponent)
result = max(x, y, z)
result = min(x, y, z)

print(result)

# Additional Math functions
print(math.pi)
print(math.e)
result = math.sqrt(x)
result = math.ceil(x) # rounds to a larger integer
result = math.floor(x)