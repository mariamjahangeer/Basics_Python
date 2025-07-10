#  Python Lists: Complete Demonstration

#  Creating a list
fruits = ["apple", "banana", "cherry", "mango"]
print("Original list:", fruits)

#  Accessing items
print("First item:", fruits[0])
print("Last item:", fruits[-1])

#  Modifying items
fruits[1] = "grape"
print("After modification:", fruits)

#  Adding items
fruits.append("orange")                  # Add to end
fruits.insert(2, "kiwi")                 # Insert at position
print("After adding items:", fruits)

#  Removing items
fruits.remove("apple")                  # Remove by value
popped_item = fruits.pop()              # Remove last item
del fruits[0]                           # Remove by index


print("After removing items:", fruits)
print("Popped item:", popped_item)

#  Looping through a list
print("List of fruits:")
for fruit in fruits:
    print("- " + fruit)

#  Useful methods
print("Index of 'kiwi':", fruits.index("kiwi"))
print("Count of 'kiwi':", fruits.count("kiwi"))

#  Sorting and reversing
fruits.sort()                           # Ascending sort
print("Sorted list:", fruits)
fruits.reverse()                        # Reverse order
print("Reversed list:", fruits)

#  Mixed-type list
random_list = [25, "hello", True, 3.14]
print("Mixed list:", random_list)

#  List length
print("Length of fruit list:", len(fruits))

# Copying and clearing
copied_list = fruits.copy()
fruits.clear()
print("Copied list:", copied_list)
print("Cleared original:", fruits)
