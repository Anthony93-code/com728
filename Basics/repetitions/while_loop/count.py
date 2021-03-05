print("How many live cables should I avoid?")
response = int(input())
iteration = 0
while iteration < response:
    iteration = iteration + 1
    print(f"Avoiding...Done! {iteration} live cables avoided.")

print("All live cables have been avoided.")