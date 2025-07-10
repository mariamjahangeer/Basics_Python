class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child(Parent):
    pass

obj = Child()
obj.greet()  # Inherits greet() from Parent


# example with super

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def show(self):
        print(f"{self.name} is in grade {self.grade}")

s = Student("Ali", 10)
s.show()


