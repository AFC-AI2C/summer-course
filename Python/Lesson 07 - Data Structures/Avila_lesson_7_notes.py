# #so you can just focus on assigning the contents to a variable
# with open('output.txt', 'r') as file_handle:
#     content = file_handle.read()

# # Open 'input.txt' in read mode and 'output.txt' in write mode using context managers
# # This ensures files are properly closed after operations
# with open('input.txt', 'r') as input, open('output.txt', 'w') as output:
# # Iterate through each line in the input file
#     for line in input:
#         # Strip whitespace from the beginning and end of the line,
#         # convert it to uppercase, add a newline character,
#         # and write it to the output file
#         output.write(line.strip().upper() + '\n')

#problem 1a
signals =[]


# with open("preclass_problem1_data.txt", "r") as in_file:

#     for line in in_file:
#         signal = int(line)
#         signals.append(signal)
# signals_sorted = sorted(signals, reverse=True)
# high_5 = signals_sorted[:5]
# corrdinate =sum(high_5) / 10.0
# print(f"the corrdinate is {corrdinate}")

  
# ## Drop in Chat to explain the flow and logic.  

# # Practice opening a file 

# # Any time you go to a problem and you need to to store somwthing you need to create a list and that list is going to need to be appended. 

# # study how to use list combine them, go through them sort them

# my_list = [1] * 5
# print(my_list)
# my_list.extend([4,5,6,7])
# print(my_list)
# second_list = ["today is monday"]
# my_list.append(second_list)
# print(my_list)
# my_list.append(list("bye"))
# print(my_list)
# my_list[0] = "change number"
# print(my_list)

# player_list = [
#     ("Jordan",  82, 15),   # (name, games_played, goals_scored)
#     ("Patel",   78, 22),
#     ("Okonkwo", 90, 18),
#     ("Li",      65, 9),
#     ("Reyes",   88, 31),
#     ("Fischer", 72, 14),
# ]
# for name, games, goals in player_list:

#     print(name)
#     print(games)
#     print(goals)

# copy_list = my_list.copy()
# print(copy_list)
# copy_list[0] = "change first text"
# print(copy_list)

# print(my_list)





soldier_data = [ 
    ("Smith", "Jacob", "SFC", 12),
    ("Taylor", "Bob", "SPC", 5),
    ("Williams", "Tom", "SGT", 6),
    ("Mac", "Tess", "1LT", 12),
    ("Snow", "Sansa", "MSG", 16),
]


unit_dict  = {"Unit": 1, "Last_name": 2, "First_name": 3,  "Rank": 4, "TIS": 5}

def look_up_soldier(unit, last_name):
    return unit, last_name

for last_name, first_name, rank, tis in soldier_data:
    display = last_name in unit_dict.items
    print(display)


#How do I get the dictonary into the FOR Loop



###############################################################################################




