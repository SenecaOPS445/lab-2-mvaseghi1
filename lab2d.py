#!/usr/bin/env python3
import sys

# Check if exactly two arguments (excluding script name) are passed
if len(sys.argv) != 3:
    print("Usage: " + sys.argv[0] + " name age")
    sys.exit()

# Assign the command line arguments to name and age
name = sys.argv[1]
age = sys.argv[2]

# Print the message
print("Hi " + name + ", you are " + age + " years old.")
