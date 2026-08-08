### Problem 1 — Basic Recursion

# **Your task:**
# - **Create a squares list using recursion**
#   - Given an integer `n`, return a list of squares from `1..n` using recursion
#   - Name your function `recursive_squares`
#   - For example, if `n=5` then the function returns `[1, 4, 9, 16, 25]`
#   - You only need to create the list using recursion, not the squares

# - **Palindrome checker**
#   - Given a string, check if it is a palindrome using recursion.  That is, is the string the same forwards and backwards, case insensitive.
#   - Name your function `palindrome_checker`
#   - For example, the input string `bacon` would return `False` while the string `radar` would return `True`.
#   - Note, for our purposes, an empty string is a palindrome.
#   - Note, for our purposes, punctuation and white space should be included.

# - **List length**
#   - Given a list, determine the length of the list using recursion
#   - Name your function `length`
#   - For example, the input list `[1, 2, 3]` would return `3`

def recursive_squares(n:int)-> list[int]:
    """Base Case"""

    if n == 0:
        return []
    if n == 1:
        return [1]

    """Recursive Step"""
    squares = recursive_squares(n -1)

    """Add number to """
    squares.append(n**2)

    return squares

# result = recursive_squares(5)
# print(result)

def palindrome_checker(string: str) -> bool:
    string = string.lower()
    # base cases
    if len(string) == 0:
        return True
    if len(string) == 1:
        return True
    if len(string) == 2 and string[0] == string[-1]:
        return True
    if string[0] != string[-1]:
        return False

    # recursive step
    result = palindrome_checker(string[1:-1])
    return result

def length(list):
    #base Case
    if len(list) == 0:
        return 0

    result =  1 + length(list[1:])
    return(result)


## Challenge Problem
def flatten(input_list: list) -> list:
    # base case
    if input_list == []:
        return []

    # work / recurse
    if isinstance(input_list[0], list):
        first_element = flatten(input_list[0])
    else:
        first_element = [input_list[0]]

    # recurse remaining elements
    remaining_elements = flatten(input_list[1:])

    result = first_element + remaining_elements
    return result


def fibonacci(n:int)-> int:

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + (n - 2)


def count_ways(n:int)->int:
    if n == 0:
        return 0
    
    if n == 1:
        return 1

    return count_ways(n-1) + count_ways(n-2)

def grid_paths(m:int, n:int)->int:
    if m == 1 or n ==1:
        return 1

    
    move_down = grid_paths(m -1, n) 
    move_right = grid_paths(m, n -1) 
    return move_down + move_right
    

    
