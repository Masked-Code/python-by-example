nested_dict = {'key1': {'subkey1': 'value1', 'subkey2': 'value2'},
               'key2': {'subkey1': 'value3', 'subkey2': 'value4'}}

D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

D = dict(emp1 = {'name': 'Bob', 'job': 'Mgr'},
         emp2 = {'name': 'Kim', 'job': 'Dev'},
         emp3 = {'name': 'Sam', 'job': 'Dev'})

print(D)
# Output: {'emp1': {'name': 'Bob', 'job': 'Mgr'},
#          'emp2': {'name': 'Kim', 'job': 'Dev'},
#          'emp3': {'name': 'Sam', 'job': 'Dev'}}

IDs = ['emp1','emp2','emp3']

EmpInfo = [{'name': 'Bob', 'job': 'Mgr'},
           {'name': 'Kim', 'job': 'Dev'},
           {'name': 'Sam', 'job': 'Dev'}]

D = dict(zip(IDs, EmpInfo))

print(D)
# Output: {'emp1': {'name': 'Bob', 'job': 'Mgr'},
#          'emp2': {'name': 'Kim', 'job': 'Dev'},
#          'emp3': {'name': 'Sam', 'job': 'Dev'}}

IDs = ['emp1','emp2','emp3']
Defaults = {'name': '', 'job': ''}

D = dict.fromkeys(IDs, Defaults)

print(D)
# Output: {'emp1': {'name': '', 'job': ''},
#          'emp2': {'name': '', 'job': ''},
#          'emp3': {'name': '', 'job': ''}}

D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

print(D['emp1']['name'])
# Output: Bob
print(D['emp2']['job'])
# Output: Dev

# key present
print(D['emp1'].get('name'))
# Output: Bob

# key absent
print(D['emp1'].get('salary'))
# Output: None

D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

D['emp3']['name'] = 'Max'
D['emp3']['job'] = 'Janitor'

print(D['emp3'])
# Output: {'name': 'Max', 'job': 'Janitor'}

D = {'emp1': {'name': 'Bob', 'job': 'Dev'}}

# Add a new key-value pair to the nested dictionary
D['emp1']['salary'] = 50000

# Add a completely new employee (nested dictionary)
D['emp2'] = {'name': 'Kim', 'job': 'Dev', 'salary': 60000}

print(D)
# Output: {'emp1': {'name': 'Bob', 'job': 'Dev', 'salary': 50000},
#          'emp2': {'name': 'Kim', 'job': 'Dev', 'salary': 60000}}

D1 = {'emp1': {'name': 'Bob', 'job': 'Dev', 'salary': 50000}}
D2 = {'emp2': {'name': 'Kim', 'job': 'Dev', 'salary': 60000}}
D1.update(D2)
print(D1)
# Output: {'emp1': {'name': 'Bob', 'job': 'Dev', 'salary': 50000},
#          'emp2': {'name': 'Kim', 'job': 'Dev', 'salary': 60000}}

D1 = {'emp1': {'name': 'Bob', 'job': 'Dev'}}
D2 = {'emp1': {'salary': 50000},
      'emp2': {'name': 'Kim', 'job': 'Dev', 'salary': 60000}}
D1.update(D2)
print(D1)
# Output: {'emp1': {'salary': 50000},
#          'emp2': {'name': 'Kim', 'job': 'Dev', 'salary': 60000}}

import collections.abc

def deep_update(source, updates):
    for key, value in updates.items():
        if isinstance(value, collections.abc.Mapping):
            source[key] = deep_update(source.get(key, {}), value)
        else:
            source[key] = value
    return source

D1 = {'emp1': {'name': 'Bob', 'job': 'Dev'}}
D2 = {'emp1': {'salary': 50000},
      'emp2': {'name': 'Kim', 'job': 'Dev', 'salary': 60000}}
deep_update(D1, D2)
print(D1)
# Output: {'emp1': {'name': 'Bob', 'job': 'Dev', 'salary': 50000},
#          'emp2': {'name': 'Kim', 'job': 'Dev', 'salary': 60000}}

D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

x = D.pop('emp3')

print(D)
# Output: {'emp1': {'name': 'Bob', 'job': 'Mgr'},
#         'emp2': {'name': 'Kim', 'job': 'Dev'}}

# get removed value
print(x)
# Output: {'name': 'Sam', 'job': 'Dev'}

D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

del D['emp3']

print(D)
# Output: {'emp1': {'name': 'Bob', 'job': 'Mgr'},
#          'emp2': {'name': 'Kim', 'job': 'Dev'}}

D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

x = D.popitem()

print(D)
# Output: {'emp1': {'name': 'Bob', 'job': 'Mgr'},
#          'emp2': {'name': 'Kim', 'job': 'Dev'}}

# get removed pair
print(x)
# Output: ('emp3', {'name': 'Sam', 'job': 'Dev'})

D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

for id, info in D.items():
    print("\nEmployee ID:", id)
    for key in info:
        print(key + ':', info[key])

# Output: Employee ID: emp1
#        name: Bob
#        job: Mgr

#        Employee ID: emp2
#        name: Kim
#        job: Dev

#        Employee ID: emp3
#        name: Sam
#        job: Dev

D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

print('emp2' in D)              # Output: True
print('name' in D['emp2'])      # Output: True