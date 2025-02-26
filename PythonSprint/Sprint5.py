# Description: Use of dictionaries in Python
# Author: Abiodun Magret Oyedele, Lana Starkes and Jeff Woolridge.
# Date(s): Feb 10, 2025 - Feb 10, 2025

'''Dictionaries in Python store key-value pairs, 
allowing fast lookups, modifications, and retrieval of data.'''

# Creating a dictionary
data = {'first name': 'Joe', 'last name': 'Shmo', 'age': 65, 
    'Province': 'Newfoundland and Labrador'}

# Accessing values
print(data['first name'])  # Joe

# Adding a new key-value pair
data['job'] = 'Student' 


# Iterating over keys and values
for key, value in data.items():
    print(key, "->", value)