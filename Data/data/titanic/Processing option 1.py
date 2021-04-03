import titanic
import display_menu


def display_passenger_names():
    print("The names of the passengers are...")
    for record in titanic.records:
        passenger_name = record[3]
        print(passenger_name)

def run():
    titanic.load_data("titanic.csv")
    num_records = len(titanic.records)
    print(f"Successfully loaded {num_records} records.")

    selected_option = display_menu.display_menu()
    print(f"You have selected option: {selected_option}")

    if selected_option == 1:
        display_passenger_names()
    else:
        print("Error! Option not recognised!")


if __name__ == "__main__":
    run()