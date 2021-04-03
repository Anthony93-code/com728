import titanic
import display_menu


def display_num_survivors():
    num_survived = int()
    for record in titanic.records:
        survival_status = int(record[1])
        if survival_status == 1:
            num_survived = num_survived + 1

    print(f"{num_survived} passengers survived")

def run():
    titanic.load_data("titanic.csv")
    num_records = len(titanic.records)
    print(f"Successfully loaded {num_records} records.")

    selected_option = display_menu.display_menu()
    print(f"You have selected option: {selected_option}")

    if selected_option == 2:
        display_num_survivors()
    else:
        print("Error! Option not recognised!")


if __name__ == "__main__":
    run()