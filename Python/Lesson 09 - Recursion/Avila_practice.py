
# First Problem 
def factorial(n: int) -> int:
    if n == 1 or n == 0:
        print("Reached Base")
        return 1
    print(f"computing chid: {n-1}")
    result = n * factorial (n-1)
    print(f"Finished child: {n- 1}")
    return result


# Second problem

def palindrome(input_str):
    if input_str == "":
        return True
    if len(input_str) == 1:
        return True

    if input_str [0] != input_str[-1]:
        return False

    print(f"computing {input_str[1:-1]}")
    result = palindrome(input_str[1:-1])
    print(f"recived {result} for {input_str[1:-1]}")
    return result

    



print(palindrome('level'))
print(palindrome("3335"))


num_list = [1,2,3,4,5]

num_list2 = [20,10,5]
def factorial(num: int) -> int:
    if num == 1 or num == 0:
            print("Reached Base")
            return 1

    print(f"Commuting Child {num-1}")
    result = num * factorial(num-1)
    print(f"finished child {num -1}")
    return result


for number in num_list:
     print(number, "factorial = ", factorial(number))

for number in num_list2:
     print(number, "factorial = ", factorial(number))


def sum_list(input_list):
     if len(input_list) == 0:
          return 0
     print(f'Eval {input_list}')
     result = sum_list (input_list[:-1]) + input_list[-1]
     print(f'recieved {result} for {input_list}')
     return result
print(sum_list([1]))
print(sum_list([1,2,3]))

