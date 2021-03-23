import csv
import sqlite3


def read_data_file(file_path):
    data = []
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            data.append(line)
    return data


def insert_in_db(data):
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()

    for item in data:
        sql = "INSERT INTO bots " \
              "(bot_name, max_speed, max_strength, creation_date, manufacturer_id)" \
              "VALUES" \
              "(?, ?, ?, ?, ?)"
        values = [item[0], item[1], item[2], item[3], item[4]]
        cursor.execute(sql, values)

    db.commit()
    db.close()


def run():
    print("Please enter a file path:")
    path = input()

    bots_data = read_data_file(path)

    print("Inserting data in to database...")
    insert_in_db(bots_data)
    print(f"Done! {len(bots_data)} records inserted.")


if __name__ == "__main__":
    run()
