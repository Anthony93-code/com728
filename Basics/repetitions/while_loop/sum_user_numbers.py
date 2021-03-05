print("How many numbers should I sum up?")
response = int(input())
summed = 0
total = 0

while summed < response:
    summed = summed + 1
    print(f"Please enter number {summed} of {response}:")
    number = int(input())
    total = total + number

print(f"The answer is {total}.")