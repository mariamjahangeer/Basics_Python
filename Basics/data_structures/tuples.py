# Tuples in Python are a type of ordered, immutable collection — meaning once created, their contents can't be changed.
# creating tuples
# Basic tuple
t1 = ("apple", "banana", "cherry")

# Mixed data types
t2 = (42, "hello", True, 3.14)

# Nested tuple
t3 = ((1, 2), ("a", "b"))

# Single-item tuple (note the comma!)
t4 = ("one",)

# accessing items
print(t1[0])     # Output: apple
print(t1[-1])    # Output: cherry

# looping through a tuple
for item in t2:
    print(item)

# slicing tuples
print(t1[1:])     # Output: ('banana', 'cherry')
print(t1[::-1])   # Output: ('cherry', 'banana', 'apple')


# tuple operstions
# Concatenation
t5 = t1 + t2

# Repetition
t6 = ("repeat",) * 3

# Length
print(len(t5))

# Membership test
print("banana" in t1)  # True


# tuple methods
t = (1, 2, 2, 3)
print(t.count(2))   # Output: 2
print(t.index(3))   # Output: 3
