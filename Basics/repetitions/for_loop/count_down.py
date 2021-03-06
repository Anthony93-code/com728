print("How far are we from the cave")
response = int(input())

for count in range(response, 0, -1):
# Added an if statement to correct grammar error when steps remaining = 1
    if count == 1:
        print(f"{count} step remaining")
    else:
        print(f"{count} steps remaining")