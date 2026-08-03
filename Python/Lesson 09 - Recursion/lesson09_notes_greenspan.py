#GitHub actions workflows are disabled by default. The top tab is actions. Click "I understand - Enable" to enable actions.

#create new branch, create new problem set file, commit
#git push origin HEAD

def factorial(n):
    if n == 1 or n == 0:
        print('base case reached')
        return 1
    print(f'computing child: {n - 1}')
    result = n * factorial(n - 1)
    print(f'finished child: {n-1}')
    return result

factorial(3)

def recurse():
    return recurse()

#Python's default maximum recursion depth is 1000.
factorial(1001)

factorial(999)

#If we recurse too far, we consume the memory.

def palindrome(input_str):
    # Defines multiple base cases.
    if input_str == "":
        return True
    if len(input_str) == 1:
        return True
    if input_str[0] != input_str[-1]:
        return False
    print(f"computing {input_str[1:-1]}")
    result = palindrome(input_str[1:-1])
    print(f"received {result} for {input_str[1:-1]}")
    return result 

print(palindrome('level'))
print(palindrome('3335'))



# Calculate the sum of a list of numbers using recursion.
def recursive_sum(my_list):
    if len(my_list) == 1: # Handles the base case.
        return 0
    print(f"computing recursive sum of {my_list}")
    result = my_list[-1] + recursive_sum(my_list[:-1])  # Handles the recursive step.
    print(f"received {result} for sum of {my_list}")
    return result

recursive_sum([1,2,3])

