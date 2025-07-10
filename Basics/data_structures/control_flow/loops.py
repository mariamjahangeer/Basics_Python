#  Python Loops: Full Demonstration

# For Loop with List
fruits = ["apple", "banana", "cherry"]
print(" For loop over list:")
for fruit in fruits:
    print("-", fruit)

#  For Loop with Range
print("\n For loop with range:")
for i in range(1, 6):
    print("Number:", i)

#  While Loop
print("\n While loop example:")
count = 0
while count < 3:
    print("Count:", count)
    count += 1

#  Break Statement
print("\n Break example:")
for i in range(5):
    if i == 3:
        print("Breaking at:", i)
        break
    print(i)

# ⏭ Continue Statement
print("\n Continue example:")
for i in range(5):
    if i == 2:
        continue
    print(i)

#  Nested Loops
print("\n Nested loop:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")

#  Loop with Else
print("\n Loop else clause:")
for i in range(3):
    print("Looping:", i)
else:
    print("No break, loop finished!")

#  While with Else
print("\n While loop with else:")
x = 0
while x < 3:
    print("x =", x)
    x += 1
else:
    print("Loop ended normally.")

#  Loop with condition and user input
print("\n Loop with input:")
attempts = 0
while attempts < 3:
    password = input("Enter password: ")
    if password == "admin":
        print(" Access granted!")
        break
    else:
        print(" Try again.")
        attempts += 1
else:
    print(" Too many failed attempts.")
