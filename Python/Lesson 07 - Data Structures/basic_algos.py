# Basic Algorithms

# Exercise 1

# What is the output of this block of code?


def mut_example(list1, list2, list3):
    if len(list1) > 2:
        list1 = list1[:2]
    list2[0] = "hi"
    list3 = "".join(list2)                  #list3 is assigned to and never used

a_list = [1, 2, 3]
b_list = ["a", "b", "c"]
a_str = "do-re-mi"
mut_example(a_list, b_list, a_str)
print(a_list)
print(b_list)
print(a_str)

```python
#expected output
[1,2]
['hi','b','c']
'hibc'          #wrong [which makes sense, there was no slicing, so changing list3 won't change a_str]
                        #but does it make sense?
```


# Exercise 2

# What's the difference between sort and sorted?

```
Source: https://docs.python.org/3/howto/sorting.html
Python lists have a built-in list.sort() method that modifies the list in-place. 
There is also a sorted() built-in function that builds a new sorted list from an iterable. 
```

# Which one is a list method and which one is a function that works on lists?
```
Sort is a list method. Sorted is a built-in function that works on lists.
```

# Please explain
```
If you want, you can do sorted((1,3,2)) which returns [1,2,3], however you can't do (1,3,2).sort().
```

# Exercise 3

# Write a function that doubles the elements in a list.

```python
#doesn't do what you want
    for val in my_list:
        val *= 2

#assuming in place
idef double2(my_list):
    for i in range(len(my_list)):
        my_list[i] *= 2

#not in place
def double(my_list):
    return [2*x for x in my_list]

def double_list_three(in_list):
    new_list = []
    for elem in in_liist:
        new_list.append(elem * 2)
    return new_list
```

# Do you need to return anything here?
```
It depends. The first case yes, the second case no.
```

# Write a function that doubles the elements in a tuple.
def double_tuple(my_tuple):
    return tuple(2*x for x in my_tuple)


# Do you need to return anything here?
```
Yes. Tuples are immutable.
```


# Exercise 4

# Rewrite the pop, count, extend, reverse, and sort functions

def my_pop(my_list):
    new_list = []
    for i in range(len(my_list)-1):
        new_list.append(my_list[i])
    return new_list

# def my_pop(in_list, index=-1):
#     #new_val = in_list[index]
#     #del in_list[index]
#     return new_val

def my_count(my_list):
    return len(my_list)

def my_len(in_list):
    len = 0
    for elem in in_list:
        len += 1
    return len 

# def my_count(in_list, obj):
#     count = 0
#     for elem in in_list:
#         if elem == obj:
#             count += 1
#     return count

def my_extend(my_list1, my_list2):
    new_list = my_list[:]
    for x in my_list_2:
        new_list.append(x) 
    return new_list

    # for elem in other_list:
    #     in_list.append(elem)

def my_reverse(my_list):
    sort_my_list = sort(my_list)
    reverse_my_list = [None] * len(my_list)
    for i in range(my_list):
        reverse_my_list[-(i+1)] = sort_my_list[i]
    return reverse_my_list

def my_reverse_two(in_list):
    for index in range(len(in_list) // 2):
        in_list[index], in_list[-index - 1] = in_list[-index - 1], in_list[index]

def my_sort(my_list):
    new_list = []
    for x in my_list:
        for i,y in enumerate(new_list):
            if 

# def bubble_sort(in_list:
#                 for start_index in range(len(in_list) - 1)

# Return the results in a new list and do not modify the original list

# (do not use the function you are rewriting)


# Exercise 5

# Fractions can be reprsented by the tuple (numerator, denominator)

# Write a function that adds two fractions



# Write a function that multiplies two fractions


# Write a function that simplifies a fraction


# Exercise 6

# write a function to calculate distance between two cartesian coordinates



# extension: make it work for more than two dimensions

