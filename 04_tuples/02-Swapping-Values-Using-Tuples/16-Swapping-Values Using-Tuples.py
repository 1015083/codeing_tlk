# Program Name: Swapping Values Using Tuples
# Purpose: This program demonstrates how to swap two numbers using tuple unpacking.
# Creator: [Nehayesh Sayedzada]
# Date: [march-26]

# Take user input for two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Store them in a tuple
numbers = (num1, num2)

# Swap the values using tuple unpacking
num1, num2 = num2, num1

# Print the swapped values
print("Swapped values:", (num1, num2))
