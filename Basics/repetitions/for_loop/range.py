print("What level of brightness is required?")
brightness_level = int(input())

print("\nAdjusting brightness...\n")

for brightness in range(2, brightness_level + 1, 2):
    symbol = brightness * '*'
    print(f"""
Beep's brightness level: {symbol}
Bop's brightness level: {symbol}
""")
print()
print("Adjustments complete!")