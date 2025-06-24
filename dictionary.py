# Dictionary  in Python

# Creating Dictionaries
dictionary = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
empty_dict = {}

# Accessing Values
print("Name:", dictionary["name"])
print("Age:", dictionary.get("age"))  # Safe access

# Modifying Dictionaries
dictionary["age"] = 31                # Update value
dictionary["job"] = "Engineer"        # Add new key-value pair
print("Modified dictionary:", dictionary)

# Removing Elements
del dictionary["city"]                 # Remove key 'city'
removed_value = dictionary.pop("job")  # Remove and return value
print("Dictionary after removals:", dictionary)
print("Removed job:", removed_value)
