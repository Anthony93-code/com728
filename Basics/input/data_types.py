print("What is your name human?")
name = input()

print("How old are you (in years)?")
age = int(input())

print("How tall are you (in meters)?")
height = float(input())

print("How much do you weigh (in kilograms)?")
weight = int(input())

print("Calculating bmi...")
bmi = float((weight / ( height**2)))

print(f"{name} you are {age} years old and your bmi is {bmi}.")

# Rounding off to 2 significant figures
print(f"{name} you are {age} years old and your bmi is {round(bmi, 2)}.")

# Alternative to 2 significant figures
print(f"{name} you are {age} years old and your bmi is {bmi: .2}.")

