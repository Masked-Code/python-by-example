f = open('myfile.csv')

# f = open(r'C:\Python33\Scripts\myfile.csv')

# Open a file for reading
f = open('myfile.csv')

# Open a file for writing
f = open('myfile.csv', 'w')

# Open a file for reading and writing
f = open('myfile.csv', 'r+')

f = open('myfile.csv')
f.close()

# check closed status
print(f.closed)
# Prints True

import csv

with open('myfile.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Prints:
# ['name', 'age', 'job', 'city']
# ['Bob', '25', 'Manager', 'Seattle']
# ['Sam', '30', 'Developer', 'New York']

import csv

with open('myfile.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Bob', '25', 'Manager', 'Seattle'])
    writer.writerow(['Sam', '30', 'Developer', 'New York'])

import csv

with open('myfile.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

# Prints:
# {'job': 'Manager', 'city': 'Seattle', 'age': '25', 'name': 'Bob'}
# {'job': 'Developer', 'city': 'New York', 'age': '30', 'name': 'Sam'}

import csv

with open('myfile.csv') as f:
    keys = ['name', 'age', 'job', 'city']
    reader = csv.DictReader(f, fieldnames=keys)
    for row in reader:
        print(row)

# Prints:
# {'job': 'Manager', 'city': 'Seattle', 'age': '25', 'name': 'Bob'}
# {'job': 'Developer', 'city': 'New York', 'age': '30', 'name': 'Sam'}

import csv

with open('myfile.csv', mode='w') as f:
    keys = ['name', 'age', 'job', 'city']
    writer = csv.DictWriter(f, fieldnames=keys)
    writer.writeheader()    # add column names in the CSV file
    writer.writerow({'job': 'Manager', 'city': 'Seattle', 'age': '25', 'name': 'Bob'})
    writer.writerow({'job': 'Developer', 'city': 'New York', 'age': '30', 'name': 'Sam'})

# Write a file with different delimiter '|'
import csv

with open('myfile.csv', mode='w') as f:
    writer = csv.writer(f, delimiter='|')
    writer.writerow(['Bob', '25', 'Manager', 'Seattle'])
    writer.writerow(['Sam', '30', 'Developer', 'New York'])

# Read a file with different delimiter '|'
import csv

with open('myfile.csv') as f:
    reader = csv.reader(f, delimiter='|')
    for row in reader:
        print(row)

# Prints:
# ['Bob', '25', 'Manager', 'Seattle']
# ['Sam', '30', 'Developer', 'New York']

import csv

with open('myfile.csv', mode='w') as f:
    writer = csv.writer(f, quotechar='"')
    writer.writerow(['Bob', '25', '113 Cherry St, Seattle, WA 98104, USA'])
    writer.writerow(['Sam', '30', '150 Greene St, New York, NY 10012, USA'])

import csv

with open('myfile.csv') as f:
    reader = csv.reader(f, quotechar='"')
    for row in reader:
        print(row)

# Prints:
# ['Bob', '25', '113 Cherry St, Seattle, WA 98104, USA']
# ['Sam', '30', '150 Greene St, New York, NY 10012, USA']

import csv, sys
filename = 'myfile.csv'
with open(filename, newline='') as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            print(row)
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

