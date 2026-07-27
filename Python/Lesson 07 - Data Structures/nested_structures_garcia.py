# Exercise 1:  Given a list of numbers, convert the list into a list of triples
# [1, 2, 3, 4, 5, 6] => [(1, 2, 3), (4, 5, 6)]
print()
my_list = [1, 2, 3, 4, 5, 6]
new_list = [tuple(my_list[:3]), tuple(my_list[3:])]
print(new_list)
print()


# Exercise 2:  Find the last element of a nested list
# [[1, 2, 3], [4, 5, 6]] => 6
nested2 = [[1, 2, 3], [4, 5, 6]]
print(nested2[-1][-1])
print()


# Exercise 3:  Create a function that lists the first N numbers in a table
# format with C columns.  Fill any remaining values with None.

import math

def table_numbers(N, C, input_table):
    row_length = math.ceil(N / C)
    counter = 0
    output_table = []
    while counter < row_length * C:
        for row in range(row_length):
            new_row = []
            for column in range(C):
                if counter < len(input_table):
                    new_row.append(input_table[counter])
                else:
                    new_row.append(None)
                counter += 1
            output_table.append(new_row)
    return output_table

# I had to look at the solutions to reverse engineer this; it would have been exceedingly difficult for me to visualize the wording/math of what was actually being asked


# Exercise 4: Create a function called make_table() that takes a number n as 
# its only parameter. Your function should create a table of size n x n 
# containing random numbers from 1 through 9.
import random

def make_table(n):
    outer_list = []
    for element in range(n):
        inner_list = []
        for nested_element in range(n):
            inner_list.append(random.randint(1,9))
        outer_list.append(inner_list)
    return outer_list
            
test_table = make_table(10)

print(test_table)
print()


# Exercise 5:  Given a list of items, write a program that generates a list of 
# lists in the following form:
# [a, b, c, ... , z] => [[z], [z, y], [z, y, x], ...]
def list_lister(input_list):
    new_list = []
    for element in range(2, len(input_list) + 2):
        new_list.append(input_list[:-element:-1])
    return new_list

input_list = list('abcdefghijklmnopqrstuvwxyz')
print(list_lister(input_list))
print()


# Exercise 6:  You have a list of numbers stored as [[1, 2, 3], [4, 5, 6]]
# Convert the numbers to their digit representation
provided_list = [[1, 2, 3], [4, 5, 6]]
stringed_list1 = ''.join([str(element) for element in provided_list[0]])
stringed_list2 = ''.join([str(element) for element in provided_list[1]])
representative_list = list((int(stringed_list1), int(stringed_list2)))
print(representative_list)
print()


# Exercise 7:  Write a function to create the tabula recta and return it
# https://www.dcode.fr/tools/vigenere/images/table.png

def rectifier():
    rect_dict = {}
    alpha_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for letter in alpha_list:
        rect_dict[letter] = alpha_list
    return rect_dict

# Call and print
rect = rectifier()
print(rect)


# Exercise 8:  Write a function to print the tabula recta in the correct format
def tabula_printer(): # I did have to check the solutions to see what was meant by "correct format"
    tabula_recta = rectifier()
    print('   ', '    '.join(tabula_recta['A'])) # Header row
    for letter in tabula_recta:
        print(letter, tabula_recta[letter])

# Call and print
tabula_printer()
print()

# Exercise 9:  Write a function to encode a message using the tabula recta
# It will need three agurments, the table, a message, and the key
# (it might be easier to write another function to "encode" a single letter
# you can then verify that against the tabula recta)

# I don't fully understand what is meant by this encoding, so I am coming up with something comparable on my own
def encoder(table, message, key):
    single_string = str(table)
    clean_string = "".join(filter(str.isalpha, single_string))
    message = message.upper()
    letter_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    encoded_message = ''
    for letter in message:
        if letter in letter_list:
            letter_index = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.find(letter)
            letter = clean_string[letter_index + 27 + key]
        else:
            letter = letter # other characters just stay
        encoded_message += letter
    return encoded_message

table = rectifier()
message = 'This problem set takes a lot of time!'
offset = 5
encoded_message = encoder(table, message, offset)
print(f"The encoded message is: {encoded_message}\n")

# Exercise 10:  Write a function to decode a message using the tabula recta
# It will need three arguments, the table, a message, and the key

def decoder(table, message, key):
    single_string = str(table)
    clean_string = "".join(filter(str.isalpha, single_string))
    message = message.upper()
    letter_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    decoded_message = ''
    for letter in message:
        if letter in letter_list:
            original_letter = clean_string[letter_list.index(letter) + 29 - key]
            letter = original_letter
        else:
            letter = letter # other characters just stay
        decoded_message += letter
    return decoded_message

table = rectifier()
message = encoded_message
offset = 5
decoded_message = decoder(table, encoded_message, offset)
print(f"The decoded message is: {decoded_message}\n")

# Probably not the exact intended decoding mechanism, but it works in a way that makes sense to me