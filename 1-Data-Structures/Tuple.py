# A tuple of integers
T = (1, 2, 3)

# A tuple of strings
T = ('red', 'green', 'blue')

# A tuple with mixed datatypes
T = (1, 'abc', 1.23, True)

# An empty tuple
T = ()

# A tuple without parentheses
T = 1, 'abc', 1.23, True

T = (4,)
print(type(T))
# Prints <type 'tuple'>

# Convert a list to a tuple
T = tuple([1, 2, 3])
print(T)
# Prints (1, 2, 3)

# Convert a string to a tuple
T = tuple('abc')
print(T)
# Prints ('a', 'b', 'c')

T = ('red', ('green', 'blue'), 'yellow')

T = ('red', 'green', 'blue', 'cyan')
print(T)
# Prints ('red', 'green', 'blue', 'cyan')

T = ('red', 'green', 'blue', 'cyan')
(a, b, c, d) = T

print(a)
# Prints red

print(b)
# Prints green

print(c)
# Prints blue

print(d)
# Prints cyan

# Swap values of 'a' and 'b'
a = 1
b = 99

a, b = b, a

print(a)
# Prints 99

print(b)
# Prints 1

# Split an email address into a user name and a domain
addr = 'bob@python.org'
user, domain = addr.split('@')

print(user)
# Prints bob

print(domain)
# Prints python.org

T = ('red', 'green', 'blue', 'yellow', 'black')

print(T[0])
# Prints red

print(T[2])
# Prints blue

T = ('red', 'green', 'blue', 'yellow', 'black')

print(T[-1])
# Prints black

print(T[-2])
# Prints yellow

T = ('a', 'b', 'c', 'd', 'e', 'f')

print(T[2:5])
# Prints ('c', 'd', 'e')

print(T[0:2])
# Prints ('a', 'b')

print(T[3:-1])
# Prints ('d', 'e')

T = (1, [2, 3], 4)
T[1][0] = 'xx'
print(T)
# Prints (1, ['xx', 3], 4)

T = ('red', 'green', 'blue')
del T

# Concatenate
T = ('red', 'green', 'blue') + (1, 2, 3)
print(T)
# Prints ('red', 'green', 'blue', 1, 2, 3)

# Replicate
T = ('red',) * 3
print(T)
# Prints ('red', 'red', 'red')

T = ('red', 'green', 'blue')
print(len(T))
# Prints 3

T = ('red', 'green', 'blue')
for item in T:
    print(item)
# Prints red green blue

T = ('cc', 'aa', 'dd', 'bb')
print(tuple(sorted(T)))
# Prints ('aa', 'bb', 'cc', 'dd')

T = ('cc', 'aa', 'dd', 'bb')
tmp = list(T)    # convert tuple to list
tmp.sort()       # sort list
T = tuple(tmp)   # convert list to tuple
print(T)         # Prints ('aa', 'bb', 'cc', 'dd')

