#pre class problem 1
import random
with open('preclass_prob_1.txt', 'w') as f:
    for i in range(100):
        line = str(random.randint(1,1000)) + '\n'
        f.write(line)

with open('preclass_prob_1.txt', 'r') as f:
    lines = f.readlines()
    maximum = -1
    minimum = 1001
    total_list = 0
    len_list = 0
    num_list = []
    for line in lines:
        number = int(line.strip())
        total_list += number
        len_list += 1
        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number
        num_list.append(number)
    #num_list = [int(line.strip()) for line in lines]
    avg_list = total_list / len_list
    print(f'Min: {minimum}\tMax: {maximum}\tAvg: {avg_list}')


#preclass problem 2
import pathlib, os
pathlib.Path('.').cwd()
os.chdir(pathlib.Path('../Lesson 04 - Strings, Advanced Functions, and Virtual Environments'))
os.system("python -m venv myvenv")
#p = pathlib.Path('.').joinpath('myvenv','Scripts','activate')
#print(p)
#os.system(str(pathlib.Path(p)))

#open bash
"""
cd into the Lesson 04 folder
Create a virtual environment there.  
Activate the virtual environment and install all of the dependencies listed in requirements.txt.  
After you do this, add this folder to your .gitignore within your repo.
"""
"""
cd '../Lesson 04 - Strings, Advanced Functions, and Virtual Environments'
python -m venv myvenv
.\myvenv\Scripts\Activate.ps1
pip list
pip install -r requirements.txt
pip list        #confirm successful installation
git status      #check what need to add to .gitignore file
echo './myvenv/' >> .gitignore       #add venv to gitignore
"""

#SyntaxError and IndentationError
print(
    for i in range(2):
        print(i)
#TypeError
1 + "1"
#ValueError
int("1+2i")
#ZeroDivisionError
0/0
#IndexError
[0,1][2]
#KeyError
{0:"a",1:"b"}[2]
#AttributeError
dir(print("a"))
print("a")._gt_
#FileNotFoundError
open("make_believe", "r")


try:
    len_ = float(input("Enter the length:  "))
    wid = float(input("Enter the width:  "))
    len_/wid
except ValueError as e:
    print(f"{e} You got a ValueError")
except ZeroDivisionError:
    print("You divided by 0")
except:
    print("There was some other error")
else:
    print("No errors")
finally:
    print("This always runs!")
    raise FileNotFoundError