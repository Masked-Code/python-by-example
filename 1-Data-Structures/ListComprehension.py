L = []
L.append(0)
L.append(1)
L.append(4)
L.append(9)
L.append(16)
print(L)
# Prints [0, 1, 4, 9, 16]

L = []
for x in range(5):
    L.append(x**2)
print(L)
# Prints [0, 1, 4, 9, 16]

L = [x**2 for x in range(5)]
print(L)
# Prints [0, 1, 4, 9, 16]

L = [x*3 for x in 'RED']
print(L)
# Prints ['RRR', 'EEE', 'DDD']

# Convert list items to absolute values
vec = [-4, -2, 0, 2, 4]
L = [abs(x) for x in vec]
print(L)
# Prints [4, 2, 0, 2, 4]

# Remove whitespaces of list items
colors = ['  red', '  green ', 'blue  ']
L = [color.strip() for color in colors]
print(L)
# Prints ['red', 'green', 'blue']

L = [(x, x**2) for x in range(4)]
print(L)
# Prints [(0, 0), (1, 1), (2, 4), (3, 9)]

# Filter list to exclude negative numbers
vec = [-4, -2, 0, 2, 4]
L = [x for x in vec if x >= 0]
print(L)
# Prints [0, 2, 4]

vec = [-4, -2, 0, 2, 4]
L = []
for x in vec:
    if x >= 0:
        L.append(x)
print(L)
# Prints [0, 2, 4]

# With list comprehension
vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
L = [number for list in vector for number in list]
print(L)
# Prints [1, 2, 3, 4, 5, 6, 7, 8, 9]

# equivalent to the following plain, old nested loop:
vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
L = []
for list in vector:
    for number in list:
        L.append(number)
print(L)
# Prints [1, 2, 3, 4, 5, 6, 7, 8, 9]

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
L = [[row[i] for row in matrix] for i in range(3)]
print(L)
# Prints [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# With list comprehension
L = [ord(x) for x in 'foo']
print(L)
# Prints [102, 111, 111]

# With list comprehension
L = [x ** 2 for x in range(5)]
print(L)
# Prints [0, 1, 4, 9, 16]

# With list comprehension
L = [x for x in range(10) if x % 2 == 0]
print(L)
# Prints [0, 2, 4, 6, 8]