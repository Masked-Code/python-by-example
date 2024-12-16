# A list of integers
L = [1, 2, 3]

# A list of strings
L = ['red', 'green', 'blue']

# A list of mixed datatypes
L = [ 1, 'abc', 1.23, (3+4j), True]

# An empty list
L = []

# Convert a string to a list
L = list('abc')
print(L)
# Prints ['a', 'b', 'c']

# Convert a tuple to a list
L = list((1, 2, 3))
print(L)
# Prints [1, 2, 3]

L = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', 'h']

L = ['red', 'green', 'blue', 'yellow', 'black']

print(L[0])
# Prints red

print(L[2])
# Prints blue

L = ['red', 'green', 'blue', 'yellow', 'black']

print(L[-1])
# Prints black

print(L[-2])
# Prints yellow

L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']

print(L[2][2])
# Prints ['eee', 'fff']

print(L[2][2][0])
# Prints eee

L = ['a', 'b', 'c', 'd', 'e', 'f']

print(L[2:5])
# Prints ['c', 'd', 'e']

print(L[0:2])
# Prints ['a', 'b']

print(L[3:-1])
# Prints ['d', 'e']

L = ['red', 'green', 'blue']

L[0] = 'orange'
print(L)
# Prints ['orange', 'green', 'blue']

L[-1] = 'violet'
print(L)
# Prints ['orange', 'green', 'violet']

L = ['red', 'green', 'yellow']
L.append('blue')
print(L)
# Prints ['red', 'green', 'yellow', 'blue']

L = ['red', 'green', 'yellow']
L.insert(1,'blue')
print(L)
# Prints ['red', 'blue', 'green', 'yellow']

L = ['red', 'green', 'yellow']
L.extend([1,2,3])
print(L)
# Prints ['red', 'green', 'yellow', 1, 2, 3]

# concatenation operator
L = ['red', 'green', 'blue']
L = L + [1,2,3]
print(L)
# Prints ['red', 'green', 'blue', 1, 2, 3]

# augmented assignment operator
L = ['red', 'green', 'blue']
L += [1,2,3]
print(L)
# Prints ['red', 'green', 'blue', 1, 2, 3]

L = ['red', 'green', 'blue']
x = L.pop(1)
print(L)
# Prints ['red', 'blue']

# removed item
print(x)
# Prints green

L = ['red', 'green', 'blue']
del L[1]
print(L)
# Prints ['red', 'blue']

L = ['red', 'green', 'blue']
L.remove('red')
print(L)
# Prints ['green', 'blue']

L = ['red', 'green', 'blue', 'red']
L.remove('red')
print(L)
# Prints ['green', 'blue', 'red']

L = ['red', 'green', 'blue', 'yellow', 'black']
del L[1:4]
print(L)
# Prints ['red', 'black']

L = ['red', 'green', 'blue']
L.clear()
print(L)
# Prints []

L = ['red']
L = L * 3
print(L)
# Prints ['red', 'red', 'red']

L = ['red', 'green', 'blue']
print(len(L))
# Prints 3

# Check for presence
L = ['red', 'green', 'blue']
if 'red' in L:
    print('yes')

# Check for absence
L = ['red', 'green', 'blue']
if 'yellow' not in L:
    print('yes')

L = ['red', 'green', 'blue']
for item in L:
    print(item)
# Prints red
# Prints green
# Prints blue

# Loop through the list and double each item
L = [1, 2, 3, 4]
for i in range(len(L)):
    L[i] = L[i] * 2

print(L)
# Prints [2, 4, 6, 8]

