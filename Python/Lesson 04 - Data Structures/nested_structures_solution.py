# Exercise 1:  Given a list of numbers, convert the list into a list of triples
# [1, 2, 3, 4, 5, 6] => [(1, 2, 3), (4, 5, 6)]
my_list = list(range(1, 7))
tuple_list = [tuple(my_list[0:3]), tuple(my_list[3:])]
print('tupled list: ', tuple_list)

# Exercise 2:  Find the last element of a nested list
# [[1, 2, 3], [4, 5, 6]] => 6
my_nested_list = [[1, 2, 3], [4, 5, 6]]
last = my_nested_list[-1][-1]
print('last element: ', last)

# Exercise 3:  Create a function that lists the first N numbers in a table
# format with C columns.  Fill any remaining values with None.

import math


def list_numbers(N, C, my_numbers):
    rows = math.ceil(N / C)
    counter = 0
    my_table = []
    while counter < rows * C:
        for row in range(rows):
            new_row = []
            for col in range(C):
                if counter < N:
                    new_row.append(my_numbers[counter])
                else:
                    new_row.append(None)
                counter += 1
                print(new_row, counter)
            my_table.append(new_row)

my_numbers = [range(25)]

print(list_numbers(16, 4, my_numbers))

# Exercise 4: Create a function called make_table() that takes a number n as its only parameter.  
# Your function should create a table of size n x n containing random numbers from 1 through 9.

# Exercise 5:  Given a list of items, write a program that generates a list of 
# lists in the following form:
# [a, b, c, ... , z] => [[z], [z, y], [z, y, x], ...]


# Exercise 6:  You have a list of numbers stored as [[1, 2, 3], [4, 5, 6]]
# Convert the numbers to their digit representation

# Exercise 7:  Write a function to create the tabula recta and return it
# https://www.dcode.fr/tools/vigenere/images/table.png

# Exercise 8:  Write a function to print the tabula recta in the correct format

# Exercise 9:  Write a function to encode a message using the tabula recta
# It will need three agurments, the table, a message, and the key
# (it might be easier to write another function to "encode" a single letter
# you can then verify that against the tabula recta)

# Exercise 10:  Write a function to decode a message using the tabula recta
# It will need three arguments, the table, a message, and the key

