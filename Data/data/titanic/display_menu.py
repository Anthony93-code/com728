import titanic

def display_menu():
    print("""
Please select one of the following options:
[1] Display the names of all passengers
[2] Display the number of passengers that survived
[3] Display the number of passengers per gender
[4] Display the number of passengers per age group
    """)
    selection = int(input())
    return selection


def run():
    titanic.load_data("titanic.csv")
    num_records = len(titanic.records)
    print(f"Successfully loaded {num_records} records.")

    selected_option = display_menu()
    print(f"You have selected option: {selected_option}")


if __name__ == "__main__":
    run()