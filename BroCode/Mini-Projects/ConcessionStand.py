menu = {
  "Poha" : 180,
  "Upma" : 180,
  "Biryani" : 200,
  "Salad" : 240,
  "Hotdog" : 45,
  "Burger" : 30,
  "Manchurian" : 210,
  "Noodles" : 200,
  "Chowmein" : 210,
  "PBM" : 240,
  "Pizza" : 240
}

order = []
total = 0

print("------------ MENU ------------")
for key, value in menu.items():
  print(f"{key:10} : Rs {value:.2f}")
print("-----------------------------")

while True:
  food = input("Select an item (q to quit): ").lower()
  if food == "q":
    break
  elif menu.get(food) is not None:
    order.append(food)

print()
print("-------YOUR ORDER-------")
for food in order:
  total += menu.get(food)
  print(food, end = " ")

print()
print(f"Total is: {total:.2f}")
