
def observed():
    observations = []
    for count in range(7):
        print("Please enter an observation:")
        obs = input()
        observations.append(obs)
    return observations

def run():
    print("Counting observation")

    # observations here is stored differently from that in the observed function as they are independent variables in each function block. could use a different name.

    observations = observed()
    observations_set = set()

    # Populate set
    for observation in observations:
        data = (observation, observations.count(observation))
        observations_set.add(data)

    for data in observations_set:
        print(f"{data[0]} observed {data[1]} times")

run()
