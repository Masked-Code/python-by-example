S = 'Hello, World!'   # single quotes
S = "Hello, World!"   # double quotes

S = """String literals can
span multiple lines."""
print(S)
# String literals can
# span multiple lines.

# an integer to a string
S = str(42)
print(S)
# Prints '42'

# a complex number to a string
S = str(3+4j)
print(S)
# Prints '(3+4j)

# a list to a string
S = str([1,1])
print(S)
# Prints '[1, 1]'

# Indexing
S = 'ABCDEFGHI'
print(S[0])    # Prints A
print(S[4])    # Prints E

# Negative Indexing
S = 'ABCDEFGHI'
print(S[-1])    # Prints I
print(S[-6])    # Prints D

S = 'ABCDEFGHI'
print(S[2:5])      # Prints CDE
print(S[5:-1])     # Prints FGH
print(S[1:6:2])    # Prints BDF

S = 'Hello, world!'
new_S = 'J' + S[1:]
print(new_S)
# Prints Jello, world!

# concatenation operator
S = 'Hello,' + ' World!'
print(S)
# Hello, World!

# augmented assignment operator
S = 'Hello,'
S += ' World!'
print(S)
# Prints Hello, World!

S = 'Hello,' " World!"
print(S)
# Prints Hello, World!

S = ('Put strings within parentheses '
    'to join them together.')
print(S)
# Put strings within parentheses to join them together.

# the hard way
S = '--------------------'

# the easy way
S = '-' * 20

S = 'Supercalifragilisticexpialidocious'
print(len(S))
# Prints 34

S = 'Hello, World!'
x = S.replace('World', 'Universe')
print(x)
# Prints Hello, Universe!

# Split the string on comma
S = 'red,green,blue,yellow'
x = S.split(',')
print(x)
# Prints ['red', 'green', 'blue', 'yellow']
print(x[0])
# Prints red

# Join the list of substrings
L = ['red', 'green', 'blue', 'yellow']
S = ','.join(L)
print(S)
# Prints red,green,blue,yellow

S = 'Hello, World!'
print(S.lower())
# Prints hello, world!

S = 'Hello, World!'
print(S.upper())
# Prints HELLO, WORLD!

S = 'Hello, World!'
print(S.capitalize())
# Prints Hello, world!

S = 'Hello, World!'
print(S.swapcase())
# Prints hELLO, wORLD!

S = 'hello, world!'
print(S.title())
# Prints Hello, World!

S = 'Hello, World!'
print('Hello' in S)
# Prints True

# Search for 'Foolish' within a string
S = 'Stay Hungry, Stay Foolish'
x = S.find('Foolish')
print(x)
# Prints 18

# Print each character in a string
S = 'Hello, World!'
for letter in S:
    print(letter, end=' ')
# H e l l o ,   W o r l d ! 

S = "We're open"		# Escape single quote
S = "I said 'Wow!'"		# Escape single quotes
S = 'I said "Wow!"'		# Escape double quotes

S = "Bob told me, \"Sam said, 'This won't work.'\""
print(S)
# Prints Bob told me, "Sam said, 'This won't work.'"

S = str('First line.\n\tSecond line.')
print(S)
# First line.
#     Second line.

S = r'C:\new\text.txt'
print(S)
# C:\new\text.txt

# printf-style % string formatting
S = '%s is %d years old.' % ('Bob', 25)
print(S)
# Prints Bob is 25 years old.

# format() Built-in Method
S = '{1} is {0} years old.'.format(25, 'Bob')
print(S)
# Prints Bob is 25 years old.

# f-String Formatter
name = 'Bob'
age = 25
S = f"{name} is {age} years old."
print(S)
# Prints Bob is 25 years old.

