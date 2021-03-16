import csv

def run(file_path):
    with open (file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        print(f"Headings:\n{headings}")
        print("Values:")
        for values in csv_reader:
            print(values)

if __name__ == "__main__":
    run("bots.csv")