# A set of strings
S = {'red', 'green', 'blue'}

# A set of mixed datatypes
S = {1, 'abc', 1.23, (3+4j), True}

S = {'red', 'green', 'blue', 'red'}
print(S)
# Prints {'blue', 'green', 'red'}

S = {1, 'abc', ('a', 'b'), True}

# Set of items in an iterable
S = set('abc')
print(S)
# Prints {'a', 'b', 'c'}

# Set of successive integers
S = set(range(0, 4))
print(S)
# Prints {0, 1, 2, 3}

# Convert list into set
S = set([1, 2, 3])
print(S)
# Prints {1, 2, 3}

S = {'red', 'green', 'blue'}
S.add('yellow')
print(S)
# Prints {'blue', 'green', 'yellow', 'red'}

S = {'red', 'green', 'blue'}
S.update(['yellow', 'orange'])
print(S)
# Prints {'blue', 'orange', 'green', 'yellow', 'red'}

# with remove() method
S = {'red', 'green', 'blue'}
S.remove('red')
print(S)
# Prints {'blue', 'green'}

# with discard() method
S = {'red', 'green', 'blue'}
S.discard('red')
print(S)
# Prints {'blue', 'green'}

S = {'red', 'green', 'blue'}
x = S.pop()
print(S)
# Prints {'green', 'red'}

# removed item
print(x)
# Prints blue

S = {'red', 'green', 'blue'}
S.clear()
print(S)
# Prints set()