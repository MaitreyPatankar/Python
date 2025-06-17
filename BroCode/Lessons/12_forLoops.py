# for loops = execute a block of code a fixed number of times.
# You can iterate over a range, string, sequence, etc.
# for (start, end, step)

# Basic Syntax
for x in range(1, 11):
    print(x)

# Reversed
for x in reversed(range(1, 11, 4)):
    print(x)
print("HAPPY NEW YEAR")

# continue = skip over an iteraion
for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

# break = come out of whole loop
for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)