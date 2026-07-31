# In-class problems and notes

def palindrome(input_str):
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

print(palindrome('racecar'))


def string_to_int(s: str) -> int:
    # Base case: single digit
    if len(s) == 1:
        return int(s)
    
    # Recursive case: convert all but last digit, multiply by 10, add last digit
    return string_to_int(s[:-1]) * 10 + int(s[-1])

print("String to Integer:")
print(f"string_to_int('1234') = {string_to_int('1234')}")
print(f"string_to_int('99') = {string_to_int('99')}")
print()


# On Your Own (practice problem) - Calculate the sum of a list of numbers using recursion

def list_sum(number_list):
    sum = 0
    for item in list:
        sum += item
    
    return sum

number_list = [1,2,3,4,5]

print(sum(number_list))

def sum_list(input_list):
    if len(input_list) == 0:
        return 0
    
    print(f"evaluating {input_list}")
    result = sum_list(input_list[:-1]) + input_list[-1]
    print(f"received {result} for {input_list}")
    return result

print(sum_list(number_list))

def list_sum_recursive(number_list: list[int]) -> int:
    if len(number_list) == 1:
        return number_list.pop()
    
    last_number = number_list.pop()
        
    return last_number + list_sum_recursive(number_list[:])

print(list_sum_recursive(number_list))




