# Set in Python

# Creating Sets
my_set = {1, 2, 3, 4, 5}
mixed_set = {1, "hello", 3.14, True}
empty_set = set()  # Note: {} creates a dictionary, not a set

# Adding Elements
my_set.add(6)
my_set.update([7, 8, 9])  # Add multiple elements
print("Updated set:", my_set)

# Removing Elements
my_set.remove(2)     # Raises KeyError if not present
my_set.discard(10)   # Does nothing if 10 is not present
removed_item = my_set.pop()  # Removes and returns an arbitrary item
print("After removals:", my_set)
print("Removed item:", removed_item)

# Set Operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference:", set_a - set_b)
print("Symmetric Difference:", set_a ^ set_b)
