numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension to filter even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

# List comprehension to square each even number
squared_numbers = [num**2 for num in even_numbers]

# Print both lists
print("Even Numbers:", even_numbers)
print("Squared Numbers:", squared_numbers)
