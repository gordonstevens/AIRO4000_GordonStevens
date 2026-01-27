import random
GLITCH_CHANCE = 0.1   # 10% chance of a sensor reading glitch!

def get_noisy_reading(base):
  if random.random() < GLITCH_CHANCE:   # If this occurred, the sensor glitched
    return 0.0
  return round(base + random.uniform(-0.5, 0.5), 2)    # Add ±0.5 cm noise to each reading, use rounding

def get_status(val):
  # if distance .= 15 -> MOVE FORWARD
  # if distance <15 and >=10 -> SLOW DOWN
  # if distance < 10 -< STOP
  # if distance = 0 -> SENSOR GLITCH - RETRY
  if val == 0:
    return 'SENSOR GLITCH - RETRY'
  elif val < 10:
    return 'STOP'
  elif val < 15:
    return 'SLOW DOWN'
  else:
    return 'MOVE FORWARD'

for i in range(1, 11):
  print(f'Checkpoint {i}:')
  
  # Generate a base then run noisy reading or glitch out using a uniform distribution
  front_sensor = get_noisy_reading(random.uniform(5, 25))   # Front sensor
  left_sensor = get_noisy_reading(random.uniform(5, 25))   # Left sensor
  right_sensor = get_noisy_reading(random.uniform(5, 25))   # Right sensor
  
  # Printing results in a readable format
  print(f'  Front sensor: {front_sensor} cm -> {get_status(front_sensor)}')
  print(f'  Left sensor: {left_sensor} cm -> {get_status(left_sensor)}')
  print(f'  Right sensor: {right_sensor} cm -> {get_status(right_sensor)}\n')
