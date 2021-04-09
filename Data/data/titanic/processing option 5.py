import titanic
import display_menu

def display_survivors_per_age_group():
    children = 0
    adults = 0
    elderly = 0
    children_survived = 0
    adults_survived = 0
    elderly_survived = 0
    for record in titanic.records:
        survived = int(record[1])
        if record[5] != "":
            age = float(record[5])
            if age < 18:
                children = children + 1
                if survived == 1:
                    children_survived += 1

            elif age < 65:
                adults = adults + 1
                if survived == 1:
                    adults_survived += 1

            else:
                elderly = elderly + 1
                if survived == 1:
                    elderly_survived += 1

    print(f"Children: {children_survived}/{children}, Adults: {adults_survived}/{adults}, Elderly: {elderly_survived}/{elderly}")


def run():
    titanic.load_data("titanic.csv")
    num_records = len(titanic.records)
    print(f"Successfully loaded {num_records} records.")

    selected_option = display_menu.display_menu()
    print(f"You have selected option: {selected_option}")

    if selected_option == 5:
        display_survivors_per_age_group()
    else:
        print("Error! Option not recognised!")


if __name__ == "__main__":
    run()