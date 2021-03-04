# Ask Beep where to search for his spare battery
print("Where should I look?")
where = input().lower().strip()

if where == "in the bedroom":
    print("Where in the bedroom should I look?")
    where_in_bedroom = input().lower().strip()
    if where_in_bedroom == "under the bed":
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery")

elif where == "in the bathroom":
    print("Where in the bathroom should i look?")
    where_in_bathroom = input().lower().strip()
    if where_in_bathroom == "in the bathtub":
        print("Found a rubber duck but no battery")
    else:
        print("Found a wet surface but no battery")

elif where == "in the lab":
    print("Where in the lab should I look?")
    where_in_lab = input().lower().strip()
    if where_in_lab == "on the table":
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery")

else:
    print("I do not know where that is but I will keep looking")