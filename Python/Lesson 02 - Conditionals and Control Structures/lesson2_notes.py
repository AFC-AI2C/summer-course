"""
These notes solve in class exercises for Python/Lesson 02.
"""

#exercise conditional statements

def cond_stmt() -> None:
    """asks a user for a number.  The script then checks the number and prints 'positive,' 'zero,' or 'negative'"""
    num = input("Input a number: ")
    while True:
        try:
            num = float(num)
            break
        except:
            print("That is not a number. Try again.")
            num = input("Input a number: ")
    if num < 0:
        print(num, "is negative")
    elif num == 0:
        print(num, "is zero")
    else:
        print(num, "is positive")

if __name__ == "__main__":
    cond_stmt()

for number in range(1, 11):
    print(number, end=" ")

my_name_list = ['Bob', "Jack", "Ryan"]
my_name_list.append('Michael')
my_name_list.append("Chris")
print(my_name_list)
my_name_list.index("Michael")
my_name_list[my_name_list.index("Michael")] = "Mike"
print(my_name_list)

for number in range(20,51,2):
    print(number, end=" ")




"""
Ask the user to input an even integer number.  
If the user puts in an odd number, print “This is an odd number”, 
and then prompt the user for an even number.  
Continue to do this until the user enters an even number.  
**Assume the user will always input an integer value**
"""
def user_int_until_even() -> None:
    user_int = int(input("Enter an even integer: "))
    while (user_int % 2) == 1:
        print("This is an odd number")
        user_int = int(input("Enter an even integer: "))

user_int_until_even()

"""
Hard code a secret integer number between 1 and 100.  
Ask the user to guess the integer.  
If they are higher then the secret number, tell them they are higher.  
If they are lower, tell them they are lower.  
When they guess it correctly, congratulate them, and end the program.
Bonus:  Display how many times the user guessed until they got it correct after they get it correct."""

def secret_number() -> None:
    secret_number = 22
    user_guess = int(input("Guess an integer number between 1 and 100: "))
    count = 1
    while user_guess != secret_number and count < 5:
        if user_guess < secret_number:
            print("Your guess was too low!")
        else:
            print("Your guess was too high!")
        user_guess = int(input("Guess an integer number between 1 and 100: "))
        count += 1
    if user_guess == secret_number:
        print(f"Congratulations, you guessed the correct number, {user_guess}")
        print(f"It took you {count} guesses.")
    else:
        print(f"Guess better next time!")

secret_number()