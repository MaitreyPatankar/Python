# collections = single "variable" used to store multiple values
# List  = [] ordered and changeable. Duplicates OK
# Set   = {} unordered and immutable, but Add/Remove OK, NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "orange", "banana", "coconut"]
print(fruits)

# to access a single entity, use index
print(fruits[0 : 3 : 2])

# iterating over list
for fruit in fruits:
  print(fruit)

# Methods in collections

# dir function - list of all methods
#print(dir(fruits))

# description of each method
#print(help(fruits))

# number of elements in list
print(len(fruits))

# if a particular element present in list
print("apple" in fruits)

# replacing elements
fruits[0] = "pineapple"
print(fruits)

fruits.insert(9, "watermelon")
print(fruits)

# adding elements at the last of list
fruits.append("pomegranate")
print(fruits)

# removing from a list
fruits.remove("banana")
print(fruits)

# sort method
fruits.sort()
print(fruits)

#reverse elements of list
# if used after sort it gives reverse alphabetical order
fruits.reverse()
print(fruits)

# lisitng out the index
print(fruits.index("pomegranate"))

# we cannot use indexing on a set because they are unordered (set object is not subscriptable)

# add element to a set
# fruits.add("melon")

# pop removes first element, but will be random
# fruits.pop()