#! bash
python -m venv test_venv

#!
py -3.10 -m venv test_venv
.\test_venv\Scripts\activate
python --version
pip install requests
pip install rich
pip list
python -m rich
deactivate

pip freeze
pip freeze >> requirements.txt

rm -r .\test_venv_

py -3.10 -m venv a_new_test_venv
git status
echo "a_new_test_venv/" >> .gitignore
git status
.\a_new_test_venv\Scripts\activate
pip list
pip install -r .\requirements.txt
pip list

deactivate
rm - .\a_new_test_venv

###In-Class Exercise #1
py -3.10 -m venv class_ex_venv
.\class_ex_venv\Scripts\activate
python --version
echo "class_ex_venv/" > .gitignore
pip install torch
pip freeze > requirements.txt
deactive
rm -r .\class_ex_venv
pip list
pip install -r .\requirements.txt

history > hist.txt
#can do ctrl + r 'query' to search for previous command with 'query' in history



my_list = ['c','a','t']
my_string = "cat"
#1. Loop over both
for item in my_list:
    print(item)

for char in my_string:
    print(char)     #same output

#2. Indexing and slicing
print(my_list[0], my_string[0])     # 'c' 'c'
print(my_list[-1], my_string[-1])   # 't' t'
print(my_strong[0:2])               # 'cat'

#3. len(), in, and membership
print(len(my_list), len(my_string)) # 3 3
print('a' in my_list, 'a' in my_string) # True True

#4. The big reveal
print(list("cat"))  # ['c', 'a', 't']



#Define the function
def validate_username(username: str) -> bool:
    #[Length Requirement] Check if the username is a certain length
    condition1 = True if len(username) >= 5 and len(username) <= 15 else False
#    print("1: ", condition1)
    #Check that it only contains numbers, letters or underscores
    #all([char.isalnum() or char == "_" for char in username])
    #username = username.replace("_", "").isalnum()
    condition2_parameters = "ABCDEFGHHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_"
    condition2 = all([(char in condition2_parameters) for char in username])
#    print("2: ", condition2)
    #Check that is starts with a letter
    # starts_with_letter = username[0].isalpha() 
    condition3_parameters = condition2_parameters[0:53]
    condition3 = username[0] in condition3_parameters
#    print("3: ", condition3)
    #Check that it does not end with an underscore
    #does_not_end_with_underscore
    condition4 = username[-1] != "_"
#    print("4: ", condition4)
    #Check that it contains at least one digit
    #has_digit = any([char.isdigit() for char in username])
    condition5_parameters = "0123456789"
    condition5 = any([(char in condition5_parameters) for char in username])
#    print("5: ", condition5)
    return all([condition1, condition2, condition3, condition4, condition5])

assert validate_username("abcdef1")
assert validate_username("ryan2360")
assert validate_username("bill")
assert validate_username("TheQuickBrownFox")

from area import rectangle_area, circle_area, tri_area

rectangle_area(10,10)
circle_area(10)
tri_area(10,10)

passengers = ["Lopez","Chen","Okafor","Smith","Patel"]
for seat, passenger in enumerate(passengers, 1):
    print(f"Seat {seat}: {passenger}")