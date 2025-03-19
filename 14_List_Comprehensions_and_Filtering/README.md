 # Given list of numbers
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

  # STEP 1: Get even numbers from the list
  even_numbers = [num for num in numbers if num % 2 == 0]

  # STEP 2: Square the even numbers
  squared_numbers = [num**2 for num in even_numbers]

  # STEP 3: Print results
  PRINT "Even Numbers:", even_numbers
  PRINT "Squared Numbers:", squared_numbers