#Part 1 - Functions
#Functions let you group instructions together and reuse them. In robotics, functions are often used for repeated actions such as move_forward() or check_sensor(). We will create functions that mimic common robot behaviors.
#Example: Greeting and Action Function
#
#def greet_and_move(name, steps):
#    print(f"Hello {name}, initiating movement.")
#    for i in range(steps):
#        print(f"Step {i+1} complete")
#
#greet_and_move("Robo1", 3)
#
#
#Exercise 1: 
#Create a function in VS Code called robot_actions.py that takes a robot’s name and number of turns, then prints a turning sequence. Call the function twice for two different robots. 

# Function to greet and move the robot
def greet_and_move(robot_name, robot_turns):
  print(f"{robot_name} responding, initiating movement.\n")
  for i in range(robot_turns):
    print(f"Step {i + 1} complete!\n")

# Gather and set information for robots
ROBOTS_QTY = 2
robots_info = {}
for i in range(1, ROBOTS_QTY+1):
  # Get information for this robot iteration
  this_robot_name = input(f'For robot #{i}, please enter a unique name for the robot: ')
  this_robot_turn_qty = int(input(f'For robot #{i}, please enter number of turns to be completed: '))
  # Set this robot into the robots info dictionary
  robots_info[this_robot_name] = this_robot_turn_qty

# Process the turns for each robot
for robot_name, robot_turn_qty in robots_info.items():
  greet_and_move(robot_name, robot_turn_qty)

print(f'All robot turns have completed successfully!')
