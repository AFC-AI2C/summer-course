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
        