def display_chars(file_path, num_chars):
    with open(file_path) as file:
        data = file.read(num_chars)
        print(f"the first 5 characters are: \n{data}")
        print("\n")


def display_line(file_path):
    with open(file_path) as file:
        data = file.readline().strip()
        print(f"The first line is: \n{data}")
        print("\n")


def display_text(file_path):
    with open(file_path) as file:
        data = file.read()
        print(f"The full text is: \n{data}")
        print("\n")


def run():
    display_chars("library.txt", 5)
    display_line("library.txt")
    display_text("library.txt")


if __name__ == "__main__":
    run()