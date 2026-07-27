#pre class problem 1
with open('preclass_problem1_data.txt','r') as f:
    lines = f.readlines()
    #.strip()
    numbers = [int(line.replace('\n','')) for line in lines]
    sorted_numbers = numbers[:]
    sorted_numbers.sort(reverse=True)
    #sorted_numbers = sorted(numbers, reverse=True)
    print(sorted_numbers)
    grid = sum(sorted_numbers[:5]) / 10
    print(f'The coordinate is {grid:.3f}')

# top_five = [-1 for i in range(5)]
# for line in lines:
#     number = int(line.replace('\n',''))
#     for i in range(4):
#         if  

# with open('preclass_problem1_data.txt','r') as in_file:
#     print(f'The coordinate is {sum(sorted(int(x) for x in in_file[-5:]) / 10}')

my_list = [1] * 5 
my_list + [6,7,8,9]
my_list.extend([6,7,8,9])
my_list
second_list = [10,20,30]
my_list.append(second_list)
my_list
my_list.extend(list("goodbye"))
my_list
my_list.append(list("goodbye"))
del my_list[0:9]
my_list
second_list[1] = 25
my_list                 #first position is a pointer to second_list
second_list[0] = 15
my_list
del second_list
my_list
                #Python has something called the garbage collector
del my_list
del second_list
my_list = [1,2,3,4,5]
second_list=[10,20,30]
my_list.append(second_list)
my_list
copy_list = my_list[:]      #shallow copy (copy simple by value, copy rest by reference), slicing ALWAYS gives a new copy, anytime you slice you create a new copy
copy_list
copy_list[2] = 30
copy_list
my_list
copy_list = my_list.copy()  #shallow copy
copy_list[2] = 30
copy_list
my_list
my_list[-1][1] = 75
my_list
copy_list
second_list[0] = 40
my_list
import copy
copy_list = copy.deepcopy(my_list)
copy_list
my_list[-1][2] = 60
my_list
second_list
copy_list
id(my_list)
id(my_list[-1])
id(second_list)

#tuples, immutable, e.g., vector
#methods: .count(), .index()
#empty tuple
()
tuple()
#parentheses are actually optional
1,2,3
#single item (trailing comma is required!)
my_tuple = (5,)     #(5,)
my_tuple = (5)      #this is just an integer
type((5))       #<class 'int'> has to do with execution order if you have ever written your own language
type((5,))
my_tuple = (5,6,7)
my_tuple
my_tuple + (8,)
my_tuple
my_list = list(my_tuple)
my_list[1] = 10
second_tuple = tuple(my_list)
second_tuple
my_tuple
del my_tuple
del second_tuple
del my_list
my_list = [10,20,30]
my_tuple (1,2,3,my_list)
my_tuple
my_list[1] = 80
my_tuple
def my_func():
    return 1, 2, 3

my_func()       #returns a tuple
type(my_func())
a, b, c = my_func()     #unpacking
a
b
c
coord = (10, 20, 30)
x, y, z = coord
x
y
z
x = x + 30
coord = (x, y, z)
coord
#can do shallow and deep copies of tuples





#O(1) big O of 1 constant time
#O(n) big O of n linear(?) time
my_set = {1,2,3,4,5}
1 in my_set
type(my_set)
second_set = {4,5,6,7,8}
my_set.union(second_set)
my_set.intersection(second_set)
my_set.difference(second_set)
my_set - second_set
my_set = set("This is my sentence of words that have letters")
for char in my_set:
    print(char)     #generally don't iterate through a set


my_dict = {}
type(my_dict)
my_dict['a'] = 1
my_dict['a']
my_dict['a'] = 2
my_dict
my_dict['b'] = 2
my_dict['c'] = [3, 4, 5]
my_dict
#my_dict[[1,2,3]] = 'nope'       #TypeError
for key in my_dict.keys():
    print(key, my_dict[key])
for key, value in my_dict.items():
        print(key, value)
for index, (key, value) in enumerate(my_dict.items()):
     value = index
my_dict         #didn't do as intended
for index, key in enumerate(my_dict.keys())):
     my_dict[key] = index
my_dict         #worked as intended
my_dict['d']        #KeyError
my_dict.get('d')    #workaround, get None back
my_dict.get('d',5)    #return 5 if not 'd' is not a key
my_dict.update([('d',5)])       #put in a list of tuples, equivalent to 'd': 5
'a' in my_dict      #tests key membership
2 in my_dict.values()
for key in my_dict:
    print(key)          #iterates through keys only
for whatever, who_cares in my_dict.items():
     print(whatever, who_cares)


#hands on #2 - dictionary
my_unit = {}
my_unit['Al'] = {'rank':"PVT", 'years_of_service':0}
my_unit['Bob'] = {'rank':"PV2", 'years_of_service':0}
my_unit['Cat'] = {'rank':"GEN", 'years_of_service':35}
my_unit['Dave'] = {'rank':"WO1", 'years_of_service':11}
my_unit['Earl'] = {'rank':"MAJ", 'years_of_service':11}
def lookup_soldier(unit, last_name):
    if unit.get(last_name) == None:                     #if last_name not in unit:
        print('The soldier was not found in the database.')
    else:
        print(f'Soldier Last Name: {last_name}\tRank: {unit[last_name]['rank']}\tYears of Service: {unit[last_name]['years_of_service']}')
lookup_soldier(my_unit, 'Al')
lookup_soldier(my_unit, 'Cat')
lookup_soldier(my_unit, 'Dimitry')
#user_input = input("Which soldier would you like to look up? ")
lookup_soldier(unit, user_input.strip())
