L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

print(L[2:7])
# Output: ['c', 'd', 'e', 'f', 'g']

L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[-7:-2])
# Output: ['c', 'd', 'e', 'f', 'g']

L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[2:-5])
# Output: ['c', 'd']

# Extract every 2nd item between position 2 to 7
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[2:7:2])
# Output: ['c', 'e', 'g']

# Return every 2nd item between position 6 to 1
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[6:1:-2])
# Output: ['g', 'e', 'c']

# Slice the first three items from the list
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[:3])
# Output: ['a', 'b', 'c']

# Slice the last three items from the list
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[6:])
# Output: ['g', 'h', 'i']

L = ['a', 'b', 'c', 'd', 'e']
print(L[::-1])
# Output: ['e', 'd', 'c', 'b', 'a']

# Modify multiple list items
L = ['a', 'b', 'c', 'd', 'e']
L[1:4] = [1, 2, 3]
print(L)
# Output: ['a', 1, 2, 3, 'e']

# Replace multiple elements in place of a single element
L = ['a', 'b', 'c', 'd', 'e']
L[1:2] = [1, 2, 3]
print(L)
# Output: ['a', 1, 2, 3, 'c', 'd', 'e']

# Insert at the start
L = ['a', 'b', 'c']
L[:0] = [1, 2, 3]
print(L)
# Output: [1, 2, 3, 'a', 'b', 'c']

# Insert at the end
L = ['a', 'b', 'c']
L[len(L):] = [1, 2, 3]
print(L)
# Output: ['a', 'b', 'c', 1, 2, 3]

# Insert in the middle
L = ['a', 'b', 'c']
L[1:1] = [1, 2, 3]
print(L)
# Output: ['a', 1, 2, 3, 'b', 'c']

# Remove elements from index 1 to 5 (exclusive)
L = ['a', 'b', 'c', 'd', 'e']
L[1:5] = []
print(L)
# Output: ['a']

# Remove elements from index 1 to 5 (exclusive)
L = ['a', 'b', 'c', 'd', 'e']
del L[1:5]
print(L)
# Output: ['a']

L1 = ['a', 'b', 'c', 'd', 'e']

# Create a shallow copy of L1
L2 = L1[:]
print(L2)
# Output: ['a', 'b', 'c', 'd', 'e']

print(L2 is L1)
# Output: False (Confirms they are different list objects)

# Attempt to slice up to index 100 (which doesn't exist)
L = ['a', 'b', 'c', 'd', 'e', 'f']
print(L[3:100])
# Output: ['d', 'e', 'f']

# Attempt to slice starting at index 5 and ending at index 3
L = ['a', 'b', 'c', 'd', 'e', 'f']
print(L[5:3])
# Output: []

