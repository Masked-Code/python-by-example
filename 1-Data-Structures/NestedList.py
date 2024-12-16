# Basic nested list
L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Nested list with different lengths of inner lists
L = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]

# Nested list with mixed data types
L = [["Alice", 30], ["Bob", 25], ["Charlie", 35]]

# Deeper nested lists
L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']

L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']

print(L[2])         # Output: ['cc', 'dd', ['eee', 'fff']]
print(L[2][2])      # Output: ['eee', 'fff']
print(L[2][2][0])   # Output: eee

L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']

print(L[-3])           # Output: ['cc', 'dd', ['eee', 'fff']]
print(L[-3][-1])       # Output: ['eee', 'fff']
print(L[-3][-1][-2])   # Output: eee

L = ['a', ['bb', 'cc'], 'd']
L[1][1] = 0
print(L)
# Output: ['a', ['bb', 0], 'd']

L = ['a', ['bb', 'cc'], 'd']
L[1].append('xx')
print(L)
# Output: ['a', ['bb', 'cc', 'xx'], 'd']

L = ['a', ['bb', 'cc'], 'd']
L[1].insert(0,'xx')
print(L)
# Output: ['a', ['xx', 'bb', 'cc'], 'd']

L = ['a', ['bb', 'cc'], 'd']
L[1].extend([1, 2, 3])
print(L)
# Output: ['a', ['bb', 'cc', 1, 2, 3], 'd']

L = ['a', ['bb', 'cc', 'dd'], 'e']
x = L[1].pop(1)
print(L)
# Output: ['a', ['bb', 'dd'], 'e']

# removed element
print(x)
# Output: cc

L = ['a', ['bb', 'cc', 'dd'], 'e']
del L[1][1]
print(L)
# Output: ['a', ['bb', 'dd'], 'e']

L = ['a', ['bb', 'cc', 'dd'], 'e']
L[1].remove('cc')
print(L)
# Output: ['a', ['bb', 'dd'], 'e']

L = ['a', ['bb', 'cc'], 'd']

print(len(L))      # Output: 3
print(len(L[1]))   # Output: 2

L = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]   
for list in L:
    for number in list:
        print(number, end=' ')
# Output: 1 2 3 4 5 6 7 8 9

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

table = [
    ["Name", "Age", "Occupation"],
    ["Alice", 30, "Engineer"],
    ["Bob", 25, "Artist"]
]

graph = [
    [1, 2],    # Neighbors of node 0
    [0, 3],    # Neighbors of node 1
    [0, 3],    # Neighbors of node 2
    [1, 2]     # Neighbors of node 3
]