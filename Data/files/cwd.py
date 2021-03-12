import os

def cwd():
    path = os.getcwd()
    print(f"The Current Working Directoryis {path}")
    print("The directory contains the following files")
    for file in os.listdir(path):
        print(file)

def run():
    print("Processing")
    cwd()

run()