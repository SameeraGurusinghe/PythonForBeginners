# This program convert user input weight into kilograms or pound (kg or lb)

weight = int(input("Enter your weight: "))
unit = input("k (kg) or l (lb) ?: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in lb = " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in KGs = " + str(converted))