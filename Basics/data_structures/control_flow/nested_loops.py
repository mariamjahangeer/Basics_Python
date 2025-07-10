#  Python Nested Loops Demonstration

#  Basic Nested For Loop
print(" Multiplication Table (1-3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("---")

#  Nested While Loop
print("\n Adding pairs using nested while:")
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"{i} + {j} = {i + j}")
        j += 1
    i += 1

#  Pattern Printing with Nested For Loops
print("\n Right-Angle Triangle Pattern:")
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

#  Nested Loops with Lists
print("\n Fruit Colors Matching:")
fruits = ["apple", "banana", "grape"]
colors = ["red", "yellow", "purple"]

for fruit in fruits:
    for color in colors:
        print(f"{fruit} might be {color}")

#  Combining Loop Types
print("\n Mixed Loops:")
for i in range(2):
    count = 0
    while count < 2:
        print(f"i={i}, count={count}")
        count += 1
