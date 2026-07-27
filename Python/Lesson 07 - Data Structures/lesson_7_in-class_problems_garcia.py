# Pre-Class Problem 1
# Input: scrambled numeric values
# Output: Grid coordinates

# # Import OS and Pathlib just in case
# import os
# from pathlib import Path

# # Read the file, strip newlines, and convert each element in the list to integers
# with open('C:/Users/Garcia/Desktop/dev/summer-course/Python/Lesson 07 - Data Structures/preclass_problem1_data.txt', 'r') as file:
#     number_list = [int(line.strip()) for line in file.readlines()]

# # Sort and get the five highest values
# number_list.sort(reverse = True)
# top_five = number_list[:5]

# # Sum and divide by 10; print the result
# enemy_grid = sum(top_five)/10
# print(f"\nThe enemy grid is {enemy_grid}\n")



# Basic Algos


# # Exercise 1

# # What is the output of this block of code?
# print(f"""
# The output is:
# [1, 2, 3]
# ['hi', 'b', 'c']
# do-re-mi
# """)

# def mut_example(list1, list2, list3):
#     if len(list1) > 2:
#         list1 = list1[:2]
#     list2[0] = "hi"
#     list3 = "".join(list2)

# a_list = [1, 2, 3]
# b_list = ["a", "b", "c"]
# a_str = "do-re-mi"
# mut_example(a_list, b_list, a_str)
# print(a_list)
# print(b_list)
# print(a_str)


# Exercise 2

# What's the difference between sort and sorted?
# Sort is a method that changes the original list, whereas sorted returns a new list

# Which one is a list method and which one is a function that works on lists?
# .sort() is a list method, and sorted() is a function that works on lists


# Exercise 3

# # Write a function that doubles the elements in a list.
# def doubler(your_list):
#     doubled_list = []
#     for element in your_list:
#         new_element = element*2
#         doubled_list.append(new_element)
#     return doubled_list

# test_list = [1,2,3,4,]
# doubled_list = doubler(test_list)
# print(doubled_list)

# Do you need to return anything here?
# Yes, but it could have been written differently so as to modify the original list and not need to return anything

# # Write a function that doubles the elements in a tuple.
# def doubler(your_tuple):
#     doubled_list = []
#     for element in your_tuple:
#         new_element = element*2
#         doubled_list.append(new_element)
#     doubled_tuple = tuple(doubled_list)
#     return doubled_tuple

# test_tuple = (1,2,3,4)
# doubled_tuple = doubler(test_tuple)
# print(doubled_tuple)

# Do you need to return anything here?
# Yes, we need to return the doubled_tuple


# Exercise 4

# Rewrite the pop, count, extend, reverse, and sort functions
# Return the results in a new list and do not modify the original list
# (do not use the function you are rewriting)

# # Redefine pop()
# def new_pop(my_list, provided_index=-1):
#     popped_list = my_list[:]
#     del popped_list[provided_index]
#     return popped_list

# # Redefine count()
# def new_count(my_list, obj):
#     counter = 0
#     for elemen in my_list:
#         if obj == elemen:
#             counter += 1
#     return counter

# # Redefine extend
# def new_extend(my_list, new_data):
#     return my_list + list(new_data)

# # Redefine reverse
# def new_reverse(my_list):
#     return my_list[::-1]

# # sort
# def new_sort(my_list):
#     sorted_list = []
#     for element in range(len(my_list)):
#         min_index = element
#         for ind in range(element + 1, len(my_list)):
#             if my_list[ind] < my_list[min_index]:
#                 min_index = ind
#         my_list[element], my_list[min_index] = my_list[min_index], my_list[element]
#     return my_list

# # Demonstrate results
# my_list = [0, 1, 2, 3]
# new_data = [4, 5, 6]
# print(f"\noriginal list: {my_list}\n")
# print(new_pop(my_list, 1))
# print(new_count(my_list, 0))
# print(new_extend(my_list, new_data))
# print(new_reverse(my_list))
# print(new_sort(my_list))


# Exercise 5
# # Fractions can be represented by the tuple (numerator, denominator)

# # Write a function that adds two fractions
# def fract_add(fract1, fract2):
#     num1, den1 = fract1[0], fract1[1]
#     num2, den2 = fract2[0], fract2[1]
#     return ((num1 * den2 + den1 * num2, den1 * den2))

# # Test it
# frac1 = (1, 2)
# frac2 = (3, 4)
# print(fract_add(frac1, frac2))

# # Write a function that multiplies two fractions
# def fract_mult(fract1, fract2):
#     num1, den1 = fract1[0], fract1[1]
#     num2, den2 = fract2[0], fract2[1]
#     return ((num1 * num2, den1 * den2))

# # Test it
# print(fract_mult(frac1, frac2))

# # Write a function that simplifies a fraction
# def fract_simp(fraction):
#     if fraction[1] % fraction[0] == 0:
#         return (1, int(fraction[1] / fraction[0]))
#     for divisor in range(fraction[0], 1, -1):
#         if fraction[0] % divisor == 0 and fraction[1] % divisor == 0:
#             return (int(fraction[0] / divisor), int(fraction[1] / divisor))
#     return fraction

# # Test it
# print(fract_simp((50,100)))


# Exercise 6
# # Write a function to calculate distance between two cartesian coordinates
# # Input: Two tuples
# # Output: Distance

# # Import math
# import math

# # Define the function for distance between two points
# def cart_dist(tup1, tup2):
#     x_dist = abs(tup2[0] - tup1[0])
#     y_dist = abs(tup2[1] - tup1[1])
#     hypotenuse = math.hypot(x_dist, y_dist)
#     return hypotenuse

# # Test it
# test_tup_a = (0, 0)
# test_tup_b = (3, 4)
# print(cart_dist(test_tup_a, test_tup_b))

# # Extension: make it work for more than two dimensions - not going to BS, I had to look at the solutions for this one
# def extra_dist(coord1, coord2):
#     root = 0
#     for value in range(len(coord1)):
#         root += (coord2[value] - coord1[value]) ** 2
#     return math.sqrt(root)

# # Test it
# coord1 = (1, 2, 3, 4)
# coord2 = (5, 6, 7, 8)
# print(extra_dist(coord1, coord2))


# # Hands-On # 2 - DICTIONARY
# # Input: name, rank, years of service for each soldier
# # Let CDR look up soldiers by their last name

# # Create dictionary
# unit = {}

# # Populate the unit dictionary with nested dictionaries (this could have been streamlined with some iteration)
# unit.update([('Matthew', dict(rank='PVT', years = 0))])
# unit.update([('Mark', dict(rank='PFC', years = 1))])
# unit.update([('Luke', dict(rank='SPC', years = 2))])
# unit.update([('John', dict(rank='SGT', years = 3))])
# unit.update([('Peter', dict(rank='CPT', years = 5))])

# # Easier syntax would have been unit["name"] = {"rank": "PVT", "years": 1}

# # Define lookup function
# def lookup_soldier(unit, last_name):
#     if last_name in unit:
#         print('Soldier found:')
#         print(last_name, unit[last_name]) # Note that formatting could be done with double indexing, like rank = unit[last_name]["rank"] and then f-strings
#     else:
#         print('Soldier could not be found')
        
# lookup_soldier(unit, 'Peter')


# # Hands-On #3: Sets
# # Input: Soldiers showing up at gate, compared to authorization list
# # Output: Authorized or not

# # Starter code (provided)
# authorized = {"Smith", "Johnson", "Williams", "Brown", "Davis"} 
# arrived = {"Smith", "Davis", "Williams", "Rodriguez"}

# # Define a function to show authorized vs. not authorized vs. didn't show up
# def security_check(authorized, arrived):
#     print(f"\nThese personnel showed up and were authorized entry: {authorized.intersection(arrived)}")
#     print(f"\nThese personnel showed up and were not authorized entry: {arrived.difference(authorized)}")
#     print(f"\nThese personnel were authorized entry but did not show up: {authorized.difference(arrived)}")
# # When reading the instructions literally, I should have made this function return all three rather than just printing, but in context, I think this makes more sense

# # Show the results
# security_check(authorized, arrived)
# print()


# # Hands-On #4: Sets and Dictionaries
# # Input: Song Lyrics
# # Output: Unique words in the song
# # Output #2: dictionary that contains each word as a key, and the number of times it shows up in your favorite song as the value

# song_string = """
# (Der Wahnsinn)
# Ist nur eine schmale Brücke
# Die Ufer sind Vernunft und Trieb
# Ich steig' dir nach
# Das Sonnenlicht den Geist verwirrt
# Ein blindes Kind, das vorwärts kriecht
# Weil es seine Mutter riecht

# (Ich finde dich)
# Die Spur ist frisch und auf die Brücke
# Tropft dein Schweiß, dein warmes Blut
# Ich seh' dich nicht, ich riech' dich nur, ich spüre dich
# Ein Raubtier, das vor Hunger schreit
# Witter' ich dich meilenweit

# Du riechst so gut
# Du riechst so gut, ich geh' dir hinterher
# Du riechst so gut
# Ich finde dich
# So gut, so gut, ich steig' dir nach
# Du riechst so gut, gleich hab' ich dich

# (Jetzt hab' ich dich)
# Ich warte, bis es dunkel ist
# Dann fass' ich an die nasse Haut
# Verrat mich nicht
# Oh, siehst du nicht, die Brücke brennt
# Hör auf zu schrei'n und wehr dich nicht
# Weil sie sonst auseinanderbricht

# Du riechst so gut
# Du riechst so gut, ich geh' dir hinterher
# Du riechst so gut
# Ich finde dich
# So gut, so gut, ich steig' dir nach
# Du riechst so gut, gleich hab' ich dich

# Du riechst so gut
# Du riechst so gut, ich geh' dir hinterher
# Du riechst so gut
# Ich finde dich
# So gut, so gut, ich fass' dich an
# Du riechst so gut, jetzt hab' ich dich
# Du riechst so gut
# Du riechst so gut, ich geh' dir hinterher
# """

# # Use set operations
# word_strings = song_string.split()
# song_set = set(word_strings)

# # Create a dictionary with counts
# from collections import Counter
# wordcounts = Counter(word_strings)

# # Print legibly
# for key, value in wordcounts.items():
#     print(f"{key}: {value}")