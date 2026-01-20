#Exercise 4:
#Create file safe_navigation.py.
# Ask the user for the number of checkpoints.
# Ensure valid integer input (negatives, zero and non-integers are not accepted).
# Then collect distances for each checkpoint, with error handling for non-numeric values.
#
#Example run:
#
#How many checkpoints? a
#Invalid input. Please enter a whole number.
#How many checkpoints? 0
#Please enter a number that is at least 1.
#How many checkpoints? 3
#Enter distance for checkpoint 1 in cm: 2
#Enter distance for checkpoint 2 in cm: 5
#Enter distance for checkpoint 3 in cm: 10
#Distances recorded: [2.0, 5.0, 10.0]

def get_checkpoints():
  qty = 0
  while True:
    try:
      while qty <= 0:
        qty = int(input("Please enter the number of checkpoints: "))
        if qty < 1:
          print('Please enter a number that is at least 1.')
      break
    except ValueError:
      print("Invalid input, please enter a whole number.")
  return qty  # Return because we have a proper integer, of value of at least 1 or greater

def check_distance(checkpoint):
  user_distance = 0
  while True:
    try:
      while user_distance <= 0:
        user_distance = int(input(f'Enter distance for checkpoint {checkpoint} in cm: '))
        if user_distance < 1:
          print('Please enter a number that is at least 1 cm.')
      break
    except ValueError:
      print("Invalid input, please enter a whole number.")
  return user_distance   # Return because we have a proper integer, of value of at least 1 or greater

checkpoints_qty = get_checkpoints()
distances = []
for i in range(1, checkpoints_qty + 1):
  distances.append(check_distance(i))

print(f'Distances recorded: {distances}')
