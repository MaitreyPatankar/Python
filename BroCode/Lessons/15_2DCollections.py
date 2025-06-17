# 2D Lists is a list made up of lists

fruits =  ["apple", "orange", "banana", "coconut"]
veggies = ["celery", "carrots", "potatoes"]
clothes = ["TShirts", "Jeans", "Shirts", "Trousers"]

cart = [fruits, veggies, clothes]

print(cart[0]) # returns fruits list

print(cart[0][0]) # returns apple

# to iterate over elements of 2D lists use nested loops

for collection in cart:
  for item in collection:
    print(item, end=" ") # space between elements
  print() # newline after every element of outer loop
