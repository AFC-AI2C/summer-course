# Basic Algorithms

# Exercise 1

### What is the output of this block of code?

```python
def mut_example(list1, list2, list3):
    if len(list1) > 2:
        list1 = list1[:2]
    list2[0] = "hi"
    list3 = "".join(list2)

a_list = [1, 2, 3]
b_list = ["a", "b", "c"]
a_str = "do-re-mi"
mut_example(a_list, b_list, a_str)
print(a_list)
print(b_list)
print(a_str)
```

```python
# output:
[1, 2, 3]
['hi', 'b', 'c']
do-re-mi
```

## Exercise 2

### What's the difference between sort and sorted?

### Which one is a list method and which one is a function that works on lists?

Solution:

sort() is a list method that operates on a list (mutable) in place. sort() returns 'None'.

sorted() is a function that takes a list as input and returns a sorted copy. The list IS NOT implicitly over-written.

## Exercise 3

### Write a function that doubles the elements in a list.

without return statement:
```python
def double(my_list):
    for i in range(len(my_list)):
        my_list[i] = 2 * my_list[i]

my_list = [1, 2, 3]
double(my_list)
print(my_list)
# output: [2, 4, 6]
```

with list comprehension (requires return statement)
```python
def double(my_list):
    return [x * 2 for x in my_list]

my_list = [1, 2, 3]
new_list = double(my_list)
print(my_list)
print(new_list)
# output: [1, 2, 3]
#         [2, 4, 6]
```

### Do you need to return anything here?

If the list is being operated on by the function, no return statement is needed. If the elements are being operated on, a return statment is needed.

### Write a function that doubles the elements in a tuple.

```python
def tuple_double(my_tuple):
    return tuple(x * 2 for x in my_tuple)

my_tuple = (1, 2, 3)
new_tuple = tuple_double(my_tuple)
print(my_tuple)
print(new_tuple)
# output: (1, 2, 3)
#         (2, 4, 6)
```

### Do you need to return anything here?

Yes, because tuple is an immutable data structure. A new tuple must be created and returned from data from the original tuple.

## Exercise 4

### Rewrite the pop, count, extend, reverse, and sort functions
```python
# pop()
def my_pop(my_list):
    return my_list[:-1]

# count()
def my_count(my_list):
    counter = 0
    for _ in my_list:
        counter += 1
    return counter

# extend
def my_extend(my_list, other_data):
    other_data = list(other_data)
    return my_list + other_data

# reverse
def my_reverse(my_list):
    return my_list(::-1)

# sort
def my_sort(my_list):
    sorted_list = []
    for i in range(len(my_list)):
        min_idx = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
    return my_list

my_list = [5, 3, 25, 4, 10]
popped = my_pop(my_list)
counted = my_count(my_list)
my_tuple = (1, 2)
extended = my_extend(my_list, my_tuple)
revrsd = my_reverse(my_list)
sortsort = my_sort(my_list)

print(popped)
print(counted)
print(extended)
print(revrsd)
print(sortsort)

'''
output:

[5, 3, 25, 4]
5
[5, 3, 25, 4, 10, 1, 2]
[10, 4, 25, 3, 5]
[3, 4, 5, 10, 25]
'''
```

### Return the results in a new list and do not modify the original list

### (do not use the function you are rewriting)


## Exercise 5

### Fractions can be reprsented by the tuple (numerator, denominator)

### Write a function that adds two fractions

### Write a function that multiplies two fractions

### Write a function that simplifies a fraction


## Exercise 6

### write a function to calculate distance between

### two cartesian coordinates

### extension: make it work for more than two dimensions
