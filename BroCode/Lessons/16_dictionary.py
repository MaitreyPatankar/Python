# dictionary = a collection of {key : value} pairs 
# ordered and changeable. No duplicates.

# print(dir(capitals)) => attributes
# print(help(capitals))

capitals = {
  "India":"New Delhi",
  "USA": "Washington DC",
  "Canada":"Ottawa",
  "China":"Beijing",
  "Japan":"Tokyo",
  "South Korea":"Seoul"
}

# Methods in dictionary

print(capitals.get("India"))
print(capitals.get("Russia")) # None

# using if with dictionary

if capitals.get("Japan"):
  print("That capital exists")
else:
  print("That capital doesn't exists")

# updating dictionary

capitals.update({"Germay":"Berlin"})
capitals.update({"USA":"New York"})

# removing a key-value pair
capitals.pop("USA")
capitals.popitem() # removes the latest key-value pair

# capitals.clear() # clears the whole dictionary

# to get all the keys excluding the values
keys = capitals.keys()
print(keys) # keys is an object

# can be iterated over keys
for key in capitals.keys():
  print(key)

# to get only values
values = capitals.values()
print(values)

# can be iterated over values
for value in capitals.values():
  print(value)

# items method
items = capitals.items()
print(items) # print 2D lists of tuples

for key, value in capitals.items():
  print(f"{key} : {value}")

# print(capitals)