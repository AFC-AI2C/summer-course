import random

# Open a file named file.txt
# "w" means write mode
# If the file doesn't exist Python creates it, if it does exist Python erases 
# everything inside it before writing new data.

with open("file.txt" , "w") as file:

# It makes Repeat 100 times, range(100) produces: That's 100 numbers, so the loop runs 100 times.

    for line in range(100):

# Generate a random number 
# This picks a random integer between 50 and 100, inclusive.

        random_number = random.randint(50,100)

# Write it to the file
        file.write(str(random_number) +'\n')
       

#Open the file again but in read mode
with open('file.txt', 'r') as input_file:

#Read every line
    lines = input_file.readlines()

#creatng the varibles you will call on 
    count  = 0
    max = 0
    min = 1000
    sum = 0

#Loop through every line
    for line in lines:
        amount = int(line)
        sum += amount
        count += 1

        if amount > max:
            max = amount

        if amount < min:
            min = amount
    average = sum /count


print(f"Max: {max}, Min: {min}, Average {average}")