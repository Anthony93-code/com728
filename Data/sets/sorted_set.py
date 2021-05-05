def observed():
    observations = []
    print("Please enter observations:")
    for count in range(5):
        obs = input()
        observations.append(obs)

    return observations


def remove_observations(observations):
  is_running = True

  while(is_running):
    print("Do you wish to remove an observation (yes/no)?")
    response = input()

    if (response == "yes"):
      print("Please enter the observation you wish to remove")
      observation = input()
      observations.remove(observation)
    else:
      is_running = False


def run():
  observations = observed()
  remove_observations(observations)

  # populate set
  observations_set = set()
  for observation in observations:
    data = (observation, observations.count(observation))
    observations_set.add(data)

  # display set
  for data in sorted(observations_set):
    print(f"{data[0]} observed {data[1]} times.")

run()