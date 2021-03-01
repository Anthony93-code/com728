# WEIGHT CONVERTER PROGRAMME (Kilogram (Kg) to pounds (lbs)
print("Please enter weight in Kg:")
weight = int(input())

print("Calculating weight...")
weight_in_lbs = float(weight / 0.45)

# Weight in lbs, rounded off to two decimal places
print(f"Weight in pounds (lbs): {round(weight_in_lbs, 2)}")

print()
print("DONE!!")
