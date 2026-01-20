# REF (Python cheat sheet): https://ehmatthes.github.io/pcc_3e/cheat_sheets/

#
# 1. Ask the user how many checkpoints to patrol (1–10).
#
def get_checkpoints():
  while True:
    try:
      # Assume input is invalid until it's valid
      qty = int(input("Please enter the number of checkpoints (1-10): "))
      if 1 <= qty <= 10:
        return qty # Valid input -> break and return
      else:
        print('Please enter a number between 1 and 10.')
    except ValueError:
      print("Invalid input, please enter a whole number.")

checkpoints_qty = get_checkpoints()

#
# 2. For each checkpoint, ask for a sensor reading (cm) and store it in a list.
#
def check_sensor_reading(checkpoint_num):
  while True:
    try:
      # Assume input is invalid until it's valid
      reading = int(input(f"Checkpoint #{checkpoint_num}: Enter sensor reading in cm: "))
      if reading > 0:
        return reading
      else:
        print('Please enter a number greater than 0.')        
    except ValueError:
      print('Invalid input, please enter a whole number.')

sensor_readings = []
for i in range(1, checkpoints_qty + 1):
  sensor_readings.append(check_sensor_reading(i)) 

#
# 3. Use a function to decide actions.
#
print("Final patrol report summary: Totals\n")   # For part 4, but it makes sense in the output to have this here.

def decide_action(distance_cm):
  if distance_cm < 10:
    return 'STOP'
  elif (distance_cm >= 10) and (distance_cm <= 14):
    return 'SLOW DOWN'
  else:
    return 'MOVE FORWARD'   # >= 15 cm

# 4.	Print a full patrol report, showing checkpoint number, distance, and action.
cnt_stop = 0
cnt_mf = 0
cnt_sd = 0

# loop for each sensor reading
for i, distance in enumerate(sensor_readings):
  # Handle NaN's or non-integers gracefully
  if not isinstance(distance, int):
    print(f'Checkpoint #{i+1}: invalid data -> skipped')
    continue   # is_nan -> continue to the next iteration
  action = decide_action(distance)  
  if action == 'STOP':
    cnt_stop += 1
  elif action == 'SLOW DOWN':
    cnt_sd += 1
  elif action == 'MOVE FORWARD':
    cnt_mf += 1
  print(f'Checkpoint #{i+1}: {distance}cm -> {action}')

print(f"Total Checkpoints: {len(sensor_readings)}\nAction counts: STOP: {cnt_stop}, SLOW DOWN: {cnt_sd}, MOVE FORWARD: {cnt_mf}")
