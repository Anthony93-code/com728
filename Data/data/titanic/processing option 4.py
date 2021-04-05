import titanic
import display_menu

def display_passengers_per_age_group():
    children = 0
    adults = 0
    elderly = 0

    for record in titanic.records:
        if record[5] != "":
            age = float(record[5])
            if age < 18:
                children += 1
            elif age < 65:
                adults += 1
            else:
                elderly += 1

    print(f"Children: {children}, Adults: {adults}, Elderly = {elderly}")


def run():
    titanic.load_data("titanic.csv")
    num_records = len(titanic.records)
    print(f"Successfully loaded {num_records} records.")

    selected_option = display_menu.display_menu()
    print(f"You have selected option: {selected_option}")

    if selected_option == 4:
        display_passengers_per_age_group()
    else:
        print("Error! Option not recognised!")


if __name__ == "__main__":
    run()