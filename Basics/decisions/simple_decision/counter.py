print("Please enter the first whole number.")
first = int(input())
print("Please enter the second whole number.")
second = int(input())
print("Please enter the third whole number.")
third = int(input())

total_even = 0
total_odd = 0

if first % 2 == 0:
    total_even = total_even + 1
else:
    total_odd = total_odd + 1

if second % 2 ==0:
    total_even = total_even + 1
else:
    total_odd = total_odd + 1

if third % 2 == 0:
    total_even = total_even + 1
else:
    total_odd = total_odd + 1

print(f"There are {total_even} even and {total_odd} odd numbers.")