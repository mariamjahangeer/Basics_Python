#  Python Modules: Full Demonstration
#  Built-in Modules
import math
import random
import datetime
import time

print(" Math Module:")
print("Square root of 25:", math.sqrt(25))
print("Value of pi:", math.pi)
print("Factorial of 5:", math.factorial(5))

print("\n Random Module:")
print("Random integer (1-10):", random.randint(1, 10))
print("Random float:", random.random())
print("Random choice:", random.choice(["apple", "banana", "cherry"]))

print("\n Datetime & Time Modules:")
print("Current time (seconds since epoch):", time.time())
print("Today's date:", datetime.date.today())


# Custom Module Example
# Let's simulate a custom module inline for demonstration
def greet(name):
    print(f"Hello, {name}! Welcome to Python Modules.")

person = {
    "name": "Ayaan",
    "age": 22,
    "country": "Pakistan"
}

print("\n Custom Module Simulation:")
greet(person["name"])
print("Person Info:", person)

