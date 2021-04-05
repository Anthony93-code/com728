import titanic
import display_menu

def display_passengers_per_gender():
    females = 0
    males = 0
    for record in titanic.records:
        gender = record[4]
        if gender == "male":
            males += 1
        elif gender == "female":
            females +=1
        else:
            print("Invalid gender!")

    print(f"Females:{females}, Males:{males}")


def run():
    titanic.load_data("titanic.csv")
    num_records = len(titanic.records)
    print(f"Successfully loaded {num_records} records.")

    selected_option = display_menu.display_menu()
    print(f"You have selected option: {selected_option}")

    if selected_option == 3:
        display_passengers_per_gender()
    else:
        print("Error! Option not recognised!")


if __name__ == "__main__":
    run()