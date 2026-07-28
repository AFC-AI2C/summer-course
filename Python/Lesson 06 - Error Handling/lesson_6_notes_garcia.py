# Lesson 6 Notes

# # Pre-Class Problem 1
# import random

# with open('rand_ints.txt', 'w') as file:
#     for line in range(100):
#         random_number = random.randint(1,1000)
#         file.write(str(random_number) + "\n")

# with open('rand_ints.txt', 'r') as input_file:
#     lines = input_file.readlines()
#     lines_stripped = [line.strip() for line in lines] # List Comprehension
#     count = 0
#     min = 1000
#     max = 0
#     sum = 0
#     for line in lines_stripped:
#         amount = int(line)
#         sum += amount
#         count += 1
#         if amount > max:
#             max = amount
#         elif amount < min:
#             min = amount
#     average = sum/count

#     print(f"Max: {max}, Min: {min}, Average: {average}")


# # In-Class Exercise #2 (not actually numbered, but on PPT #15)
# import random
# import math

# # Randomly generate a secret number, with a seed for testing purposes
# random.seed(0)
# random_number = random.randint(1,100)

# # Initialize a wrong guess to start the loop, count, and guess list
# user_guess = 0
# count = 0
# abs_dist = 0

# # Print header
# print()
# print('=== GUESSING GAME ===')
# print()

# # Guessing game, but this time wrap it in try except
# while user_guess != random_number:
#     try:
#         user_guess = input('Guess a number (1-100): ')
#         if not user_guess.lstrip('-').isdigit():
#             print("Your guess is not the right data type.")
#         else:
#             user_guess = int(user_guess)
        
#         abs_dist = math.fabs((user_guess - random_number))
        
#         if user_guess < 0:
#             raise ValueError('Guess cannot be negative.')
#         elif user_guess > 100 or user_guess == 0:
#             raise ValueError('Guess is outside of range and must be 1-100.')
#         elif abs_dist <= 10:
#             hint = 'HOT!'
#         elif abs_dist <= 20:
#             hint = 'WARM'
#         elif abs_dist <= 40:
#             hint = 'COLD'
#         else:
#             hint = 'ICE COLD'
        
#         print(f"Hint: {hint}\n")
#         count += 1
    
#     except TypeError:
#         print(f"You must enter an integer.\nPlease try again.\n")
    
#     except ValueError as e:
#         print(f"An error occurred: {e}\nPlease try again.\n")

# if user_guess == random_number:
#     print(f"""CORRECT! The secret number was: {random_number}
# You guessed it in {count} non-error tries.
# """)


# Exercise 3
# Input: List of numbers
# Output: Prints a new list without None values or non-integer types

# Given list and new list placeholder
given_list = [10, -5, 20, 'hello', 5.2, 15, None, 30]
processed_list = []

# For loop to do all the work, to include error handling
for element in given_list:
    try:
        if isinstance(element, type(None)):
            raise TypeError(f"Skipped 'None' at index {given_list.index(element)}")
        elif not isinstance(element, int):
            raise TypeError(f"Skipped non-integer type at index {given_list.index(element)}")
        elif element < 0:
            raise ValueError(f"Negative number found at index {given_list.index(element)}")
            # I am not stopping the program here, because it can continue with errors handled gracefully, also preventing the need to delete -5 later
        else:
            processed_list.append(element)
    except TypeError as e:
        print(f"Caught an error: {e}")
    except ValueError as e:
        print(f"Caught an error: {e}")

print(f"\nHere is the new list of integers only: {processed_list}\nIts sum is: {sum(processed_list)}\n")