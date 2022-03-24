# Based on https://youtu.be/HGOBQPFzWKo?t=1790 

# DICTIONARY data structure : Key-Value pairs, unordered, mutableeexit

import utils_edchin.pyxlib as sysx
sysx = sysx()
sysx.clear_terminal()
# ----------------------------

# Creating Dictionaries.....
print('Creating Dictionaries.....')
# using curly braces
dict_1 = {"name":"Ed",
            "age":"55",
            "city":"New York"
          }
print('\ndict_1:\n',dict_1)

# using the dict() function
dict_2 = dict(name="Ed",
                age=50,
                city='Houston')
print('\ndict_2:\n',dict_2) 

# Get values using keys
print('\n Get values using keys.....')
value = dict_1['name']
print('value of key="name" :', value)

# Modify values using keys
print('\n Modify values using keys.....')
dict_1["name"]='Eddie'
print('new value of key="name" :', dict_1["name"])

# Delete key pairs
print('\n Deleting key pairs.....')

del dict_1["name"]
#     OR
dict_1.pop("age")
dict_2.popitem() # removes last item

print(dict_1)
print(dict_2)

# Adding key pairs
print('\n Adding key pairs.....')
dict_1["name"] = "Edgar"
dict_1["age"] = 60
dict_2["city"] = 'Austin'
print(dict_1)
print(dict_2,'\n')

# Test if key exists
keys = {'name', 'age', 'zip', 'city'}
for key in keys:
    if key in dict_1:
        print(key, ':', dict_1[key])
    else:
        print(key, 'key does not exists')

