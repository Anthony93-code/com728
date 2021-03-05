print("Please enter a number?")
response = int(input())
count = 0
total = 1

while count < response:
    count = count + 1
    total = total * count

print(f"The factorial is {total}.")
