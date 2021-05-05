
sequence = {"Short Sequence": 3, "Medium Sequence": 2, "Long Sequence": 1}

def display_keys(data):

    for key in data.keys():
        print(key)


def display_values(data):
    for value in data.values():
        print(value)


def display_items(data):
    for key, value in data.items():
        print(f"{key}: {value}")

def run():
    print("Keys:")
    display_keys(sequence)
    print("\nValues:")
    display_values(sequence)
    print("\nPairs:")
    display_items(sequence)

run()