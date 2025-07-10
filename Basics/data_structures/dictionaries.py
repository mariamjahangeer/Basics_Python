student = {
    "name": "Ali",
    "age": 20,
    "is_enrolled": True
}

# Common Dictionary Operations
# Accessing values
print(student["name"])  # Output: Ali

# Adding a new key-value pair
student["grade"] = "A"

# Updating existing value
student["age"] = 21

# Removing a key
del student["is_enrolled"]

# Using .get() to safely access keys
print(student.get("address", "Not found"))

# Checking if key exists
print("grade" in student)  # Output: True


# Looping Through a Dictionary
for key in student:
    print(key, "=>", student[key])

# Or use .items()
for key, value in student.items():
    print(f"{key}: {value}")


