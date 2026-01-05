# Calculate the factorial of n using linear recursion
# Logic: n! = n * (n-1) * (n-2)... * 1
# Base Case: If n is 0 or 1, return 1.

def factorial(n: int) -> int:
        pass


# Sum a list of integers by processing one element at a time.
# Uses recursion to 'pop' the last element and add it 
# to the sum of the remaining list.

def re_sum_one(num_list: list[int]) -> int:
    pass


# Sum a list using a 'Divide and Conquer' approach.
# Split the list into two halves and recursively sums each half 
# until single elements are reached, then adds them back together.

def re_sum_half(num_list: list[int]) -> int:
        pass


# Calling this will result in a RecursionError because it lacks a 
# base case to stop the function from calling itself.

'''
def bad():
    return bad()

bad()
'''

# Calculate the nth Fibonacci number using tree recursion.
# Sequence: 0, 1, 1, 2, 3, 5, 8, 13...
# Returns the sum of the two preceding numbers in the sequence.

def fib(n: int) -> int:
    """
    0, 1, 2, 3, 4, 5, 6,  7,  8, ...
    0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    """

# Perform a recursive binary search on a sorted array.
# Divide the search interval in half repeatedly. If the value of the 
# search key is less than the item in the middle of the interval, 
# narrow the interval to the lower half. Otherwise, narrow it to the upper half.

def binary_search(arr, low, high, x):
    pass


# Test array for binary search
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")


# Recursively list all files in a directory and its subdirectories.
# This acts as a 'crawler' that enters every folder it finds 
# to print the full paths of the files hidden inside.

import os

def list_dir_recursive(directory):


# list_dir_recursive('/my_folder')