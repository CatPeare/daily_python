person = {"name": "Alice", "age": 25, "city": "New York"}

# Accessing values
print(person["name"])  # Output: "Alice"
print(person["age"])  # Output: 25
print(person.get("city"))  # Output: "New York"
print(person.keys()) # Output: dict_keys(['name', 'age', 'city'])
print(person.values()) # Output: dict_values(['Alice', 25, 'New York'])

# Modifying values
person["age"] = 26
print(person)  # Output: {"name": "Alice", "age": 26, "city": "New York"}

# Adding new key-value pairs
person["occupation"] = "Software engineer"
print(person)  # Output: {"name": "Alice", "age": 26, "city": "New York", "occupation": "Software engineer"}

# Looping over keys and values
for key, value in person.items():
    print(f"{key}: {value}")

# Let's access the first key of the dictionary
keys = list(person.keys())  # Convert keys into a list
first_key = keys[0]  # Access the first element in the list
print(first_key)  # Output: "name"

# Same method for value
values = list(person.values())  # Convert keys into a list
first_value = values[0]  # Access the first element in the list
print(first_value)  # Output: "name"

'''
Alternatively, you can use the next() function with the iter() function
to get the first key in the dictionary without converting the keys into a list. 
'''
person = {"name": "Alice", "age": 25, "city": "New York"}
first_key = next(iter(person))
print(first_key)  # Output: "name"
