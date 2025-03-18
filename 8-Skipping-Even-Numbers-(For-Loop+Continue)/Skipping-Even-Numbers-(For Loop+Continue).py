# Program Name: skipping_even_numbers.py
# Purpose: Print numbers from 1 to 10 but skip even numbers
# Creator: Nehayesh Sayedzada
# Date: 2025-03-14

# Loop from 1 to 10
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)
