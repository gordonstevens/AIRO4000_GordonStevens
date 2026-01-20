# Create a function in VS Code called robot_actions.py that takes a robot’s name and number of turns, then prints a turning sequence. Call the function twice for two different robots. 
distances_qty = 5
distances = []

def decide_action(distance):
  if distance < 10:
    return "STOP"
  elif distance < 15:
    return "SLOW DOWN"
  else:
    return "MOVE FORWARD"

for i in range(1, distances_qty + 1):
  distances.append(int(input(f'Please enter a distance for movement #{i} of {distances_qty} movements in cm: ')))

# REF (Python cheat sheet): https://ehmatthes.github.io/pcc_3e/cheat_sheets/
for distance in distances:
  print(f'{distance} cm: {decide_action(distance)}')
