
def observed():
    observations = []
    print("Please enter observations:")
    for count in range(7):
        obs = input()
        observations.append(obs)

    return observations

def run():
    print("counting observations...")
    observations = observed()
    obs = set()
    for letter in observations:
        letter_occurrence = letter, observations.count(letter)
        obs.add(letter_occurrence)
    print(obs)
if __name__ == "__main__":
    run()