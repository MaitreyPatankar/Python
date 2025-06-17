# while loop = executes some code WHILE some condition remains true

#Example 1
name = input("Enter your name: ")

while name == "":
  print("You did not enter your name")
  name = input("Enter your name: ")
  
print(f"Hello {name}")

# Example 2
age = input("Enter your age: ")

while age < 0:
  print("Age cannot be negative")
  age = input("Enter your age: ")
else:
  print(f"You are {age} years old")

# Example 3
food = input("Enter a food you like (q to quit): ")

while not food == "q":
  print(f"You like {food}")
  food = input("Enter a food you like (q to quit): ")

print("Bye")

# Example 4
num = int(input("Enter a number between 1 - 10: "))

while (1 > num  or num > 10):
  print(f"{num} is not valid")
  num = int(input("Enter a number between 1 - 10: "))

print(f"Your number is {num}")