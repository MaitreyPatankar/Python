import random

# print(help(random))

low = 1
high = 100

number = random.randint(low, high)
print(number)

# for random floating point number 0 to 1
float_number = random.random()
print(float_number)

options = ("rock", "paper", "scissors")
print(random.choice(options))


# shuffle method
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
random.shuffle(cards)
print(cards)
