print("Please enter the number of lives.")
lives = int(input())

print("Please enter the energy level.")
energy = int(input())

print("Please enter the shield level.")
shield = int(input())

print(f"""
Health has been set.

Lives:  {lives * "♥"}
Energy: {energy * "♦"}
Shield: {shield * "@"}
""")
