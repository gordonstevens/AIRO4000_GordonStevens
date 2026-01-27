#Create robot_log.py:
#1. Ask the user for 3 readings for each of 3 sensors: front, left, right.
#2. Store them in a nested dictionary (sensor name → list of readings).
#3. Print how much each sensor’s reading has changed from first to last.

def get_sensor_reading(iteration):
  while True:
    try:
      # Assume input is invalid until it's valid
      sensor_reading = float(input(f'  Reading {iteration}: '))
      if sensor_reading >= 0:   # Valid if 0cm or greater
        return sensor_reading   # Valid input -> break and return
      else:
        print('Please enter the measurement (0 or greater).')
    except ValueError:
      print('Invalid input, please enter a number.')

sensors = {"front": [], "left": [], "right": []}

for sensor in sensors.keys():
  print(f'\nPlease enter three readings for the {sensor} sensor (cm):')
  for i in range(3):
    reading = get_sensor_reading(i+1)
    sensors[sensor].append(reading)

print(f'\n--- Sensor Change Report ---')

for sensor, readings in sensors.items():
  first = readings[0]
  last = readings[-1]
  change = last - first
  status = 'increase' if change >= 0 else 'decrease'
  print(f'{sensor.capitalize()}: {first:.2f} -> {last:.2f} (change {change:+.2f} cm, {status})')

print(f'\nAll readings:')
for sensor, readings in sensors.items():
  print(f'{sensor.capitalize()}: {readings}')
