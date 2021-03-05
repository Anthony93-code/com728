print("How many bars should be charged?")
response = int(input())
charge = 0

while charge < response:
    charge = charge + 1
    bar_charge = charge * "█ "
    print(f"Charging: {bar_charge}")

print("The battery is fully charged.")
