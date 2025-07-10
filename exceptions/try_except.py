# try:
#     # Code that might raise an error
#     risky_operation()
# except SomeError:
#     # Code to run if an error occurs
#     handle_error()


try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# Catching Multiple Exceptions
try:
    print(x)
except NameError:
    print("Variable x is not defined.")
except Exception as e:
    print("Something went wrong:", e)

# using else and finally
try:
    print("No errors here!")
except:
    print("Caught an error.")
else:
    print("This runs only if no exception occurs.")
finally:
    print("This always runs, error or not.")


# Raising Your Own Exceptions
x = -5
if x < 0:
    raise ValueError("x must be non-negative")


# Real-World Example: File Handling
try:
    with open("data.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("File operation complete.")