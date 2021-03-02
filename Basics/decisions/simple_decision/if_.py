print("What type of book is this?")
type_of_book = input()

# Added .lower() function to ignore the case of the input; also added .strip() function to ignore any spaces entered by the user in the input
if type_of_book.lower().strip() == "adventure":
    print("I like adventure books!")

print("Finished reading book.")