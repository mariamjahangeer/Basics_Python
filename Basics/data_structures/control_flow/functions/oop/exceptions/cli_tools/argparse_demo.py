# The argparse module in Python is a built-in library used to create command-line interfaces (CLIs)

import argparse

# Create parser object
parser = argparse.ArgumentParser(description="Square a number")

# Add argument
parser.add_argument("number", type=int, help="Number to square")

# Parse arguments
args = parser.parse_args()

# Use the argument
print(f"The square of {args.number} is {args.number ** 2}")




