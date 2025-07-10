class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):  # Constructor
        self.name = name            # Instance attribute
        self.age = age

    def bark(self):                # Method
        print(f"{self.name} is barking!")


# Creating objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

# Accessing attributes and methods
print(dog1.name)         # Output: Buddy
print(dog2.species)      # Output: Canine
dog1.bark()              # Output: Buddy is barking!

# using str method
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

dog1 = Dog("Buddy", 3)
print(dog1)  # Output: Buddy is 3 years old.