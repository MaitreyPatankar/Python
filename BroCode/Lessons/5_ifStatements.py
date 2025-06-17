# if = Do some code only if condition is true
# else do something else

age = int(input("Enter your age: "))

if age > 100:
  print("Agle janam me aana")

elif age > 18:
  print("Eligible for credit card")

elif age < 0:
  print("Paida to ho ja")

else:
  print("Grow up kid")

# Use of booleans with if statements
for_sale = True

if for_sale:
  print("This item is for sale")
else:
  print("This item is NOT for sale")