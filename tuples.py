# Tuples in Python

# Creating Tuples
my_tuple = (1, 2, 3)
mixed_tuple = (1, "hello", 3.14)
single_element_tuple = (42,)  # Note the comma
empty_tuple = ()

# Accessing Elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Looping Through a Tuple
print("Looping through tuple:")
for item in my_tuple:
    print(item)

# Tuple Operations
print("Length:", len(my_tuple))
print("Concatenation:", my_tuple + (4, 5))
print("Repetition:", my_tuple * 2)

# Tuple Unpacking
a, b, c = my_tuple
print("Unpacked:", a, b, c)

# Using Tuples as Dictionary Keys
tuple_key_dict = {
    (1, 2): "point A",
    (3, 4): "point B"
}
print("Value for key (1, 2):", tuple_key_dict[(1, 2)])
