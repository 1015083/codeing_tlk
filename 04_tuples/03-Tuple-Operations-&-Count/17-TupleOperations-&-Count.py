# Program Name: Tuple Operations & Count
# Purpose: This program demonstrates how to count the occurrences of a value in a tuple.
# Creator: [Nehayesh-Sayedzada]
# Date: [march-27]

# Creating a tuple with repeated values
fruit_tuple = ("apple", "banana", "apple", "cherry", "banana", "apple")

# Ask the user to input a fruit name
fruit = input("Enter a fruit name: ")

# Count how many times the fruit appears in the tuple
fruit_count = fruit_tuple.count(fruit)

# Print the result
print(f"'{fruit}' appears {fruit_count} times in the tuple.")
