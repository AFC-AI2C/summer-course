# from math import pi, ceil
# def patio_design() -> None:
#     diameter = float(input("Enter the diameter (feet): "))
#     total_area = pi * (diameter/2) ** 2
#     print(f"The area of the patio is {total_area:.2f} square feet.")
#     brick_l = 4/12
#     brick_w = 6/12
#     brick_area = brick_l * brick_w
#     num_bricks = total_area/brick_area
#     print(f"""The patio needs {ceil(num_bricks)} bricks (4" x 6" size).""")

# patio_design()


# def count_char_x(word: str, trgt_char: str) -> int:
#     return sum([char == trgt_char for char in word])

# count_char_x("California", "i")


### Review Session - Problem 3

from string import ascii_uppercase
def pw_strength(pw: str) -> str:
    digits = "0123456789"
    has_digit = any([char in digits for char in pw])
    has_upper = any([char in ascii_uppercase for char in pw])
    if len(pw) < 8:
        strength = "Weak" 
    elif has_digit == False and has_upper == False:
        strength = "Weak"
    elif has_digit == False or has_upper == False:
        strength = "Medium"
    else: 
        strength = "Strong"
    print(f"The strength is {strength}")
    return(strength)

my_pw = input("Enter your password: ")
while (pw_strength(my_pw) != "Strong"):
    my_pw = input("Enter your password: ")




# ### Review Session - Problem 4
# def letter_grade(score: int) -> str:
#     if score >= 90:
#         return "A"
#     elif score >= 80:
#         return "B"    
#     elif score >= 70:
#         return "C"    
#     elif score >= 60:
#         return "D"    
#     else:
#         return "F"

# print(letter_grade(95))
# print(letter_grade(85))
# print(letter_grade(75))
# print(letter_grade(65))
# print(letter_grade(55))

# try:
#     students = int(input("How many grades are there to enter? "))
#     total_scores = 0
#     for student in range(1, students+1):
#         score = float(input(f"Enter student #{student}'s score: "))
#         total_scores += score
#         print(f"Student number #{student} got a letter grade  {letter_grade(score)}")

#     print(f"The class average was {total_scores/students:.1f}, this is a a {letter_grade(total_scores/students)}")
# except ZeroDivisionError as e:
#     print("There were no students")

def letter_grade(score: int) -> str:
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"    
    elif score >= 70:
        return "C"    
    elif score >= 60:
        return "D"    
    else:
        return "F"

class Tests:
    def __init__(self):
        self.counter = 0
        self.scores = []
        self.total_score = 0
        self.grade = ""
    def new_test(self, score):
        self.counter += 1
        self.scores.append(score)
        self.total_score += score
        self.avg_score = sum(self.scores)/self.counter
        self.grade = letter_grade(sum(self.scores)/self.counter)

class Test:
    def __init__(self, score, tests_tracker):
        self.score = score
        self.letter_grade = letter_grade(self.score)
        tests_tracker.new_test(self.score)

my_tests = Tests()
my_tests.__dict__
test1 = Test(100, my_tests)
test1.__dict__
my_tests.__dict__
test2 = Test(70, my_tests)
my_tests.__dict__