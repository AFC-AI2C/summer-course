"""This module demonstrates basic Python calculations."""

def add_together(num1, num2):
    """ adding both veribles together. """
    new_num = num1 + num2
    return new_num

if __name__ == "__main__":
    RESULT = add_together(10, 20)
    print(RESULT)


# new problem
lenght = int(input("Enter the base of the rectangle: "))
width = int(input(" Enter the width of the rectangle: "))


# the :int lets it know we are expexcting intergers.
def area_retangle(lenght1: int, width1: int) -> int:
    """ Area Recangle Caculation"""
    area = lenght1 * width1
    return area


answer = area_retangle(lenght, width)
print(f" the area is {answer}")


total = float(input("input the toatl amount of your bill: "))
tip_percentage = float(input("What percentage you want to tip: "))

#find Tip amount
def tip(bill_total: float, percentage: float) -> float:
    """Tip Cacaulations with percentage"""
    percentage = percentage / 100
    amount = bill_total * percentage
    return amount


tip_amount = tip(total, tip_percentage)
print(f" Baseed on you total cost of {total} you should tip {tip_amount:.02f}")


def has_more_characters(first_word: str, second_word: str) -> str:
    """The lenght of the words"""
    first_length = len(first_word)
    second_length = len(second_word)

    if first_length < second_length:
        return f"Second_word has {second_length} characters"

    if first_length > second_length:
        return f"first_word has {first_length} characters"

    return f"they are equal both strings have {first_length} characters"


if __name__ == "__main__":
    MORE_CHARACTERS = has_more_characters("sally", "tom")
    print(MORE_CHARACTERS)


# need to helpwith these make it also show how many characteres it is


# need to know Visiual Studio Code: how to create vitrtual network.

# Thursday 1330 Class
# Friday 1030 Class
