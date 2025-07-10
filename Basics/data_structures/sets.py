#  Python Sets: Full Demonstration

#  Creating sets
colors = {"red", "green", "blue", "green"}  # 'green' appears only once
print(" Original Set:", colors)

#  Accessing elements (via loop, since sets are unordered)
print(" Looping through set:")
for color in colors:
    print("-", color)

#  Adding elements
colors.add("yellow")
colors.update(["purple", "orange"])  # Add multiple items
print(" After adding:", colors)

# ➖ Removing elements
colors.discard("green")   # Safe removal
colors.remove("red")      # Will raise error if 'red' not found
popped = colors.pop()     # Removes a random item
print(" After removing:", colors)
print(" Popped item:", popped)

#  Clearing the set
temp_set = {"a", "b", "c"}
temp_set.clear()
print(" Cleared set:", temp_set)

#  Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print(" Union:", a | b)
print(" Intersection:", a & b)
print(" Difference (a - b):", a - b)
print(" Symmetric Difference:", a ^ b)

#  Frozenset (immutable set)
frozen = frozenset(["apple", "banana", "cherry"])
print(" Frozenset:", frozen)

# Membership test
print(" Is 'banana' in frozen?", "banana" in frozen)


