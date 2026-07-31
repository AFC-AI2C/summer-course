# problem 1
temp = float(input("What is the current Tempautre: "))
rain = input("is it raining: (Y/N) ").upper()
if temp >= 40:
    output = "Wear a coat"
elif temp <= 65:
    output = "Bring a jacket. "
else:
    output = "Enjoy Weather"
if rain == "Y":
    output += " Bring an ubrella"

print(output)

# problem 2
# # lesson notes for lesson 3
start_input = int(input("enter start number: "))
end_input = int(input("enter end number: "))

def fizz_buzz(beg: int, end: int) -> int:
    counter = 0
    for number in range(beg, end+1):
        if number % 3 == 0 and number % 5 == 0:
            print(f"fizz_Bizz {number} \n")
            counter += 1
        elif number % 3 == 0:
            print(f"Fizz {number} \n")
        elif number % 5 == 0:
            print(f"Buzz {number}\n")
        else:
            print(f"{number} \n")

    return counter

count = fizz_buzz(start_input, end_input)
print(f"There were {count} fizz_buzz numbers \n")


#Work on this becacse its not looping

#problem 3
#check password

password = input("enter passwrd a stong password: ")


def password_checker (password: str) ->str:
    len_password = len(password)
    if len_password < 8:
        return "password weak less than 8 characters, needd to be longer"
        
    
    has_digit = False
    has_letter = False

    for char in password:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_digit = True

    if has_letter and has_digit:
        return "Strong"    
    
    else:
        return "password meduim, need to add a digit to secure it"
        

print(password_checker(password))


# Put the while loop out side the defintion, it wii keep running until the results say strong.  
# by putting it "while true" means it will always be true until it says break. 
while True:
    password = input("enter passwrd: ")

    results = password_checker(password)

    print(results)

    if results == "Strong":
        print("Great Job, you created a stong password")
        break

# the \n makes the next line skip so there is more space
    print("try again.\n")



# Problem 4

student = int(input("How many grades would you like to put in: "))



def letter_grades (score):
    if score >= 90:
        return"A" 
    elif score >=80:
        return "B"
    elif score >=70:
        return "C"
    elif score >=60:
        return "D"
    else:
        return "F"

#make grade have list is saving it so I can call it back
       
grades =[]

for i in range(student):
    print(f"Enter you grade for student # {i + 1}")

    grade = float(input("Enter student grade percentage: "))

# appending it keeping each grade saved that is input

    grades.append(grade)



    print(f"Students # {i + 1} letter grades is {letter_grades (grade)}")

print ("----- Summary ------")

print(f" All the grade are: {grades}")
print(f" The highest grade is: {max(grades)}")
print(f" The lowest grade is: {min(grades)}")
print(f" The average score is: {sum(grades) /len(grades):.02f}")




