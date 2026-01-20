distances = [12, 8, 'Meow', 15, 5, 20, 51, 75, 2, 9, 36, 15]

cnt_stop = 0
cnt_mf = 0
cnt_sd = 0

def decide_action(distance_cm):
  if distance_cm < 20:
    return 'STOP'
  elif distance_cm >= 50:
    return 'MOVE FORWARD'
  else:
    return 'SLOW DOWN'

for i, distance in enumerate(distances):
  # Handle NaN's: If so skip the entry gracefully
  if not isinstance(distance, (int)):   # REF (Python isinstance() Function): https://www.w3schools.com/python/ref_func_isinstance.asp
    print(f'Reading {i}: invalid -> skipped')
    continue # Force the next iteration

  action = decide_action(distance)
  if action == 'STOP':
    cnt_stop += 1
  elif action == 'MOVE FORWARD':
    cnt_mf += 1
  elif action == 'SLOW DOWN':
    cnt_sd += 1
  print(f'Reading {i}: {distance}cm -> {action}')

print(f'\nSummary:\nSTOP: {cnt_stop}, SLOW DOWN: {cnt_sd}, MOVE FORWARD: {cnt_mf}')
