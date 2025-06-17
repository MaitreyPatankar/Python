# format specifiers = {value : flags} format a value based on what flags are inserted

# .(number)f - round to that many decimal spaces (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator

price1 = 349805.14159
price2 = -39348.8945
price3 = 3234224.433

# number of digits to be shown after decimals
print(f"Price 1 is {price1:.2f}") 
print(f"Price 2 is {price2:.3f}")
print(f"Price 3 is {price3:.1f}")

# to insert spaces from left side
print(f"Price 1 is {price1:10}") 
print(f"Price 2 is {price2:20}")
print(f"Price 3 is {price3:30}")

# to insert zero from left side or we can say zero padded
print(f"Price 1 is {price1:010}") 
print(f"Price 2 is {price2:020}")
print(f"Price 3 is {price3:030}")

# left justify
print(f"Price 1 is {price1:<10}") 
print(f"Price 2 is {price2:<20}")
print(f"Price 3 is {price3:<30}")

# right justify = default
print(f"Price 1 is {price1:>10}") 
print(f"Price 2 is {price2:>20}")
print(f"Price 3 is {price3:>30}")

# center justify = default
print(f"Price 1 is {price1:^10}") 
print(f"Price 2 is {price2:^20}")
print(f"Price 3 is {price3:^30}")

# to display sign
print(f"Price 1 is {price1:+}") 
print(f"Price 2 is {price2:+}")
print(f"Price 3 is {price3:+}")

# thousand seperator
print(f"Price 1 is {price1:,}") 
print(f"Price 2 is {price2:,}")
print(f"Price 3 is {price3:,}")

# combining operators
print(f"Price 1 is {price1:+,.3f}") 
print(f"Price 2 is {price2:0,.7f}")
print(f"Price 3 is {price3:<,.4f}")