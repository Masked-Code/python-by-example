# Break the for loop at 'blue'
colors = ['red', 'green', 'blue', 'yellow']
for x in colors:
    if x == 'blue':
        break
    print(x)
# Prints red green

# Break the while loop when x becomes 3
x = 6
while x:
    print(x)
    x -= 1
    if x == 3:
        break
# Prints 6 5 4

# Break the for loop at 'blue'
colors = ['red', 'green', 'blue', 'yellow']
for x in colors:
    if x == 'blue':
        break
    print(x)
else:
    print('Done!')
# Prints red green

# Break the while loop when x becomes 3
x = 6
while x:
    print(x)
    x -= 1
    if x == 3:
        break
else:
    print('Done!')
# Prints 6 5 4

# in a for statement
for x in range(5):
  try:
      print('trying...')
      break
      print('still trying...')
  except:
      print('Something went wrong.')
  finally:
      print('Done!')
# Prints trying...
# Prints Done!

# in a while statement
while 1:
  try:
      print('trying...')
      break
      print('still trying...')
  except:
      print('Something went wrong.')
  finally:
      print('Done!')
# Prints trying...
# Prints Done!