# List in Python

# Creating Lists
my_list = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]
empty_list = []

# Accessing Elements
print("First element:", my_list[0])       # 1
print("Last element:", my_list[-1])        # 5

# Modifying Lists
my_list.append(6)                          # Add 6 at the end
my_list.insert(2, 99)                      # Insert 99 at index 2
print("After append and insert:", my_list)

my_list.remove(3)                          # Remove the first occurrence of 3
popped_item = my_list.pop()               # Remove last item
print("After remove and pop:", my_list)
print("Popped item:", popped_item)

# Looping Through a List
print("Looping through list:")
for item in my_list:
    print(item)