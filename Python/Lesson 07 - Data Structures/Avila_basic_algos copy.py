# Basic Algorithms

# Exercise 1

# What is the output of this block of code?


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

# sort reorders the orginal list, works only on list, gives no return'
# sorted creates a copy of list and reorders, works on list, tuples, will return a new list

# Which one is a list method and which one is a function that works on lists?

# sort is a list method and sorted is a function

# Please explain



# Exercise 3

# Write a function that doubles the elements in a list.

# def double_function(my_list):
#     return [x * 2 for x in my_list]

# def double_function(my_list):
#     new_list = []
#     for elm in my_list:
#         new_list.append(elm * 2)

#     return new_list



def print_each_name_twice(names):
    new_list =[]
    for name in names:
        new_list.append(name)
        new_list.append(name)

    return new_list

players=["James", "Matthew", "Joshua"]

call_my_function = print_each_name_twice(players)

print("This is my Double List ")
for names in call_my_function:
    print(names)

print(players)







# # Do you need to return anything here?
# double_list = double_function(a_list)
# print(f"{double_list} .\n")





# # Write a function that doubles the elements in a tuple.
# def tuple_double(my_tuple):
    
#     return [x * 2 for x in my_tuple]

def tuple_double(my_tuple):
    return my_tuple * 2



my_turple = ("James", "Matthew", "Joshua")

double_my_turple = tuple_double(my_turple)

print(double_my_turple)



# Do you need to return anything here?



# Exercise 4

# Rewrite the pop, count, extend, reverse, and sort functions

#Basic use of Pop:
removed_player_using_pop = players.pop()

print(removed_player_using_pop)
print(players)

#Pop in a function

def remove_last_item_in_myList(myList) :
    return myList.pop(0)

players=["James", "Matthew", "Joshua"]

last_player_removed = remove_last_item_in_myList(players)

print("Player Removed",last_player_removed)
print("Players Reamining", players)



#Count function How many times a specific item appears
def count_function(my_list, item):
    return my_list.count(item)

players=["James", "Matthew", "Joshua", "James"]
player_count = count_function(players, "James")

print(player_count)
print(players)

# Extend in a function (adds multiple items from another list to the end of a list.)
# append() adds ONE item ## extend() adds multiple items:
def extend_in_a_function(my_list, items):
    my_list.extend(items)
    return my_list

players=["James", "Matthew", "Joshua", "James"]
new_list = extend_in_a_function(players,[ "tommy", "sara"])  #(New names added are in bracket, it adding a new list to the end)

print(new_list)


# reverse function 

def my_reverse_function(my_list):
    my_list.reverse()
    return my_list

players=["James", "Matthew", "Joshua", "Danny"]

my_revrsed_list = (my_reverse_function(players))

print(my_revrsed_list)

# reverse function using slicing 

def my_reverse_function(my_list):

    return my_list[::-1]

players=["James", "Matthew", "Joshua", "Danny"]

my_revrsed_list = (my_reverse_function(players))

print(my_revrsed_list)



# a sort function

def my_sort_function(my_list):
    my_list.sort()  #to reverse the sort (reverse=True)
    return my_list

players=["James", "Matthew", "Joshua", "Danny"]

sorted_players =my_sort_function(players)

print(sorted_players)


# Exercise 5

# Fractions can be reprsented by the tuple (numerator, denominator)

# Write a function that adds two fractions

def two_fractions_function (numerator1:float, denominator1:float, numerator2:float, denominator2:float)-> float:
    answer = (numerator1 /denominator1) + (numerator2/denominator2)
    return answer

problem = two_fractions_function(10,2,5,2)

print(problem)

# Write a function that multiplies two fractions

def multi_two_fractions_function (numerator1:float, denominator1:float, numerator2:float, denominator2:float)-> float:
    answer = (numerator1 /denominator1) * (numerator2/denominator2)
    return answer

problem = multi_two_fractions_function(10,2,5,2)

print(problem)


# Write a function that simplifies a fraction
import math
def simplifies_fraction (numerator1, denominator1):
    divisor = math.gcd(numerator1, denominator1)

    numerator1= numerator1 //divisor
    denominator1 = denominator1 //divisor
    return numerator1, denominator1 

problem = simplifies_fraction(10,20)


print(problem)


# Exercise 6

# write a function to calculate distance between two cartesian coordinates



# extension: make it work for more than two dimensions

