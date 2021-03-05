print("Please enter a phrase:")
response = input()

number_of_characters = len(response)
number_of_display = 0
while number_of_display < number_of_characters:
    number_of_display += 1
    print("Bop ", end="")