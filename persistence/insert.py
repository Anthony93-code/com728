import sqlite3

def get_bot_from_user():
    print("Please enter bot name")
    name = input()

    print("Please enter bot speed")
    speed = int(input())

    print("Please enter bot strength")
    strength = int(input())

    print("Please enter bot date")
    date = input()

    print("Please enter manufacturer")
    manufacturer = int(input())

    return [name, speed, strength, date, manufacturer]


def insert_bot_in_db(data):
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()

    sql = "INSERT INTO bots " \
          "(bot_name, max_speed, max_strength, creation_date, manufacturer_id) " \
          "VALUES (?, ?, ?, ?, ?)"

    values = [data[0], data[1], data[2], data[3], data[4]]
    cursor.execute(sql, values)
    row_id = cursor.lastrowid
    db.close()

    print("The record has been added to the database.")
    print(f"Id of new record is {row_id}")


def run():
    data = get_bot_from_user()
    insert_bot_in_db(data)


if __name__ == "__main__":
    run()