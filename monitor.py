# SECTION: Vars and helper
ROBOT_CHK_QTY_MIN = 1
ROBOT_CHK_QTY_MAX = 5
robotspeedlist = {}

# Create function for checking speed
def check_speed(speed):
  if speed < 10:
    return "Too slow" 
  elif speed > 50:
    return "Too fast"
  else:
    return "Speed OK" 

# SECTION: Ask user for number of robots to check 
print("Gordon's Robot Monitor.\n\n")
robotqty = int(input(f"How many robots would you like to check? Please enter a number between {ROBOT_CHK_QTY_MIN} and {ROBOT_CHK_QTY_MAX}: "))

# SECTION: Check number of robots to check
if robotqty < ROBOT_CHK_QTY_MIN or robotqty > ROBOT_CHK_QTY_MAX:
  print(f"Please enter the number of robots to check, between {ROBOT_CHK_QTY_MIN} and {ROBOT_CHK_QTY_MAX} robots to check.")
else:
  # Ask for each robot entry
  for i in range(ROBOT_CHK_QTY_MIN, robotqty+1):
    irobotspeed = int(input(f"For robot #{i} of {robotqty}, please enter the speed in cm/s: "))
    robotspeedlist[i] = check_speed(irobotspeed)

  # SECTION: Display speed check results
  print(f"--- Results for {robotqty} robots ---\n")
  for robot_num, robot_speedcheck in robotspeedlist.items():
    print(f"Robot #{robot_num}'s speed is {robot_speedcheck}")