def identify():
    print("What do you see?")
    response = input().lower().strip()
    if response == "a loud boulder":
        print("It's time to run!")
    else:
        print("We will be fine.")

identify()