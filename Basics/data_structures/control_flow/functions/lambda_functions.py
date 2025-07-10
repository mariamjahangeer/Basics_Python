# Lambda functions in Python are anonymous, one-line functions defined using the lambda keyword
square = lambda x: x ** 2
print(square(5))  # Output: 25


add = lambda x, y: x + y
print(add(3, 7))  # Output: 10

# map
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)  # Output: [2, 4, 6, 8]

# filter
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: [2, 4, 6]

# sorted
students = [("Ali", 85), ("Sara", 92), ("Zara", 78)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students)

