import random


with open("file.txt" , "w") as file:
    
    for line in range(100):
        random_number = random.randint(50,100)
        file.write(str(random_number) +'\n')
       

with open('file.txt', 'r') as input_file:
    lines = input_file.readlines()
    count  = 0
    max = 0
    min = 1000
    sum = 0

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