# logical operators = evaluate multiple conditions (and, or, not)
# or = at least one condition must be true
# and = all conditions must be true
# not = inverts the condition

# OR operator
temp = float(input("Enter temperature in Celcius"))
is_raining = True

if (temp > 35) or (temp < 0) or is_raining:
    print("The outdoor event is cancelled")
else:
   print("The outdoor event is still scheduled")

# AND operator
is_sunny = True

if(temp >= 28) and is_sunny:
    print("It is HOT outside")
    print("It is SUNNY")
elif (temp <= 0) and is_sunny:
    print("It is COLD outside")
    print("It is SUNNY")
elif (28 > temp > 0) and is_sunny:
    print("It is WARM outside")
    print("It is SUNNY")

# NOT operator
elif(temp >= 28) and not is_sunny:
    print("It is HOT outside")
    print("It is CLOUDY")
elif (temp <= 0) and not is_sunny:
    print("It is COLD outside")
    print("It is not CLOUD")
elif (28 > temp > 0) and not is_sunny:
    print("It is WARM outside")
    print("It is not CLOUD")