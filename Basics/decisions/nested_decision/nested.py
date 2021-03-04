# Ask Beep for type of book Cover
print("What type of cover does the book have (hard/soft)?")
cover_type = input().lower().strip()

if cover_type == "soft":
    print("Is the book perfect-bound (yes/no)?")
    perfect_bound = input().lower().strip()
    if perfect_bound == "yes":
        print("Soft cover, perfect bound books are very popular!")
    elif perfect_bound == "no":
        print("Soft covers with coils or stitches are great for short books")
    else:
        print("INVALID OPTION")
elif cover_type == "hard":
    print("Books with hard covers can be more expensive!")
else:
    print("INVALID OPTION")