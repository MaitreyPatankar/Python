# nested loop = A loop within another loop (outer, inner)
# by default print statement ends with a newline character

# Example 1
for x in range(3):
  for y in range(1, 10):
    print(y, end = "") # for printing every element in the same line
  print()

# Example 2 - Print a rectangle
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
  for y in range(cols):
    print(symbol, end = "") # for printing every element in the same line
  print()
