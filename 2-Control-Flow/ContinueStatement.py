# skip 'blue' while iterating a list
colors = ['red', 'green', 'blue', 'yellow']
for x in colors:
    if x == 'blue':
        continue
    print(x)
# Prints red green yellow

# Print values from 6 through 0 while skipping odd numbers
x = 6
while x:
	x -= 1
	if x % 2 != 0:
		continue
	print(x)
# Prints 4 2 0

# in a for Statement
for x in range(2):
  try:
      print('trying...')
      continue
      print('still trying...')
  except:
      print('Something went wrong.')
  finally:
      print('Done!')
print('Loop ended.')
# Prints trying...
# Prints Done!
# Prints trying...
# Prints Done!
# Prints Loop ended.

# in a while statement
x = 2
while x:
  try:
      print('trying...')
      x -= 1
      continue
      print('still trying...')
  except:
      print('Something went wrong.')
  finally:
      print('Done!')
print('Loop ended.')
# Prints trying...
# Prints Done!
# Prints trying...
# Prints Done!
# Prints Loop ended.

