import csv
LOG_FILE_NAME = 'log.csv'

# Check each input for appropriate value
def get_sensor_reading(iteration):
  while True:
    try:
      sensor_reading = float(input(f'  Reading {iteration}: '))
      if sensor_reading >= 0:
        return sensor_reading
      else:
        print('Please enter the measurement (0 or greater).')
    except ValueError:
      print('Invalid input, please enter a number.')

# Initiate dictionary of sensors
sensors = {'front': [], 'left': [], 'right': []}

# Ask user for readings
for sensor in sensors.keys():
  print(f'\nPlease enter three readings for the {sensor} sensor (cm):')
  for i in range(3):
    #reading = get_sensor_reading(i+1)
    sensors[sensor].append(get_sensor_reading(i+1))

# Write readings to CSV file
with open(LOG_FILE_NAME, 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(['front', 'left', 'right'])  # Write headers
  for i in range(3):   # Write measurements
    writer.writerow([sensors['front'][i], sensors['left'][i], sensors['right'][i]])

# Show readings loaded in from CSV
print(f'\nData saved to {LOG_FILE_NAME}')

sensor_readings_from_csv = {'front': [], 'left': [], 'right': []}
with open(LOG_FILE_NAME, 'r') as file:
  reader = csv.DictReader(file)
  for row in reader:   # Read in each row
    for key in sensor_readings_from_csv.keys():
      sensor_readings_from_csv[key].append(float(row[key]))

print('\n--- Loaded Readings ---')
for sensor, readings in sensor_readings_from_csv.items():   # This prints format as discussed in the document, Average, Min, and Max values
  avg = sum(readings) / len(readings)
  minimum = min(readings)
  maximum = max(readings)
  print(f'{sensor.capitalize()} - Avg: {avg:.2f} cm, Min: {minimum:.2f} cm, Max: {maximum:.2f} cm')
