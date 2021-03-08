print("How many rows should I have")
rows = int(input())
print()
print("How many columns should I have")
columns = int(input())
print()
print("Here I go:")
print()
emoji = ":-)"

for count in range(0, rows, 1):
    for number in range(0, columns, 1):
        print(emoji, end="")
# Add an additional empty print statement indented to the outer 'for' loop to allow for a new line character to be displayed after the inner loop has completed execution.
    print()
print()
print("Done!")