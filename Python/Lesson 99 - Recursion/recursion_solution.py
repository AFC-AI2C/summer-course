# Calculate the factorial of n using linear recursion
# Logic: n! = n * (n-1) * (n-2)... * 1
# Base Case: If n is 0 or 1, return 1.

from re import search

def factorial(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    print(f"Calculating {n} * {n - 1}!")
    return n * factorial(n - 1)

ninenine = factorial(99)
print(ninenine * 100)

# Sums a list of integers by processing one element at a time.
# This function uses recursion to 'pop' the last element and add it 
# to the sum of the remaining list.

def re_sum_one(num_list: list[int]) -> int:
    print("Entering another recursion")
    if len(num_list) == 1:
        return num_list.pop()

    last = num_list.pop()
    print(f"Calculating {num_list[:]} + {last}")
    val = re_sum_one(num_list[:])
    print(f"Finished recursion for {num_list[:]}")
    return val + last


max = 10
numbers = list(range(1, max + 1))
print(re_sum_one(numbers[:]))


# Sums a list using a 'Divide and Conquer' approach.
# Splits the list into two halves and recursively sums each half 
# until single elements are reached, then adds them back together.

def re_sum_half(num_list: list[int]) -> int:
    if len(num_list) == 1:
        return num_list[0]

    half = len(num_list) // 2
    print(f"Calculating {num_list[:half]} + {num_list[half:]}")
    return re_sum_half(num_list[:half]) + re_sum_half(num_list[half:])

print(re_sum_half(numbers[:]))

# An example of infinite recursion.
# Calling this will result in a RecursionError because it lacks a 
# base case to stop the function from calling itself.

def bad():
    return bad()

# bad()

# Calculates the nth Fibonacci number using tree recursion.
# Sequence: 0, 1, 1, 2, 3, 5, 8, 13...
# Returns the sum of the two preceding numbers in the sequence.

def fib(n: int) -> int:
    """
    0, 1, 2, 3, 4, 5, 6,  7,  8, ...
    0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    """
    if n == 0:
        return 0
    if n == 1:
        return 1

    print(f"Calculating fib({n-1}) + fib({n-2})")
    return fib(n - 1) + fib(n - 2)


print(fib(6))

# Performs a recursive binary search on a sorted array.
# Divides the search interval in half repeatedly. If the value of the 
# search key is less than the item in the middle of the interval, 
# narrow the interval to the lower half. Otherwise, narrow it to the upper half.

def binary_search(arr, low, high, x):
    """assumes array is already sorted"""
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")


import os

# Recursively lists all files in a directory and its subdirectories.
# This acts as a 'crawler' that enters every folder it finds 
# to print the full paths of the files hidden inside.

def list_dir_recursive(directory):
    for entry in os.listdir(directory):
        full_path = os.path.join(directory, entry)
        if os.path.isdir(full_path):
            list_dir_recursive(full_path)
        else:
            print(full_path)

# list_dir_recursive('/my_folder')
