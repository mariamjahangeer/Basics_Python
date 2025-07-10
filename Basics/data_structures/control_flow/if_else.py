#  Python if-else statements: Full Demonstration

#  User Input
number = int(input("Enter a number: "))

#  Basic if-else
if number > 0:
    print("Positive number")
elif number == 0:
    print("Zero")
else:
    print("Negative number")

#  Multiple conditions
age = int(input("\nEnter your age: "))
if age >= 18:
    print("You're an adult.")
elif 13 <= age < 18:
    print("You're a teenager.")
else:
    print("You're a child.")

#  Nested if statements
score = int(input("\nEnter your score (0-100): "))
if score >= 60:
    print("You passed!")
    if score >= 90:
        print("Excellent work!")
else:
    print("You failed. Try again!")

#  Inline condition (Ternary Operator)
x = int(input("\nEnter a value for x: "))
result = "Even" if x % 2 == 0 else "Odd"
print(f"{x} is", result)

#  Logical operators
day = input("\nEnter a day: ").lower()
if day == "saturday" or day == "sunday":
    print("It's the weekend!")
else:
    print("It's a weekday.")

#  Boolean flags
logged_in = input("\nAre you logged in? (yes/no): ").lower() == "yes"
if logged_in:
    print("Welcome back!")
else:
    print("Please log in to continue.")
