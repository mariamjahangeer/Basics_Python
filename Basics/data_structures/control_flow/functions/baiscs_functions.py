# 🔹 Basic Function
def greet():
    print("Hello, welcome to Python!")

greet()

#  Function with Parameters
def welcome(name):
    print(f"Hello, {name}!")

welcome("Ayaan")

# Function with Return Value
def add(x, y):
    return x + y

result = add(5, 3)
print("Sum is:", result)

# Function with Default Argument
def introduce(name, country="Pakistan"):
    print(f"My name is {name} and I am from {country}.")

introduce("Ali")
introduce("Sara", "Canada")

#  Keyword Arguments
def describe_pet(name, type):
    print(f"{name} is a {type}")

describe_pet(type="dog", name="Bruno")

#  Variable-length Arguments (*args)
def total(*numbers):
    print("Numbers received:", numbers)
    return sum(numbers)

print("Total is:", total(10, 20, 30))

# Variable-length Keyword Arguments (**kwargs)
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_info(name="Zara", age=21, grade="A")

#  Lambda Function (Anonymous function)
square = lambda x: x ** 2
print("Square of 6 is:", square(6))

#  Function with Condition
def check_even(num):
    return num % 2 == 0

print("Is 4 even?", check_even(4))

#  Recursive Function
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))
