print("Towards which direction should I paint (up, down, left or right)?")
direction = input()

if direction.lower().strip() == "up":
    print("\nI am painting in the upward direction!")
elif direction.lower().strip() == "down":
    print("\nI am painting in the downward direction")
elif direction.lower().strip() == "left":
    print("\nI am painting in the left direction")
elif direction.lower().strip() == "right":
    print("\nI am painting in the right direction")
else:
    print("\nUnknown Direction")

print("\nDONE!")