print("Please enter your full name:")
full_name = input()

print("Please enter your year of birth:")
birth_year = int(input())
age = 2021 - birth_year

if age >= 18 and age <= 30:
    print("Please Enter nationality:")
    nationality = input().lower().strip()
    if nationality == "nigerian":
        print("how did you hear about us?")
        how = input().lower().strip()
        if how == "website" or how == "friend":
            print(f"{full_name}, your identity has been verified and you are qualified. Congrats!")
        else:
            print(f"Welcome {full_name}! \nHowever, your identity require further verification.")
    else:
        print("ONLY FOR NIGERIANS")
elif age << 18 or age == 30:
    print(f"{full_name}, you are {age} year(s) old. \nUnfortunately, we will not be progressing your request any further.")
else:
    print("Sorry, you are stuck!")