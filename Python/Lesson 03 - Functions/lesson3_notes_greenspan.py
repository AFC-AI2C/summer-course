from math import pi, ceil
def patio_design() -> None:
    diameter = float(input("Enter the diameter (feet): "))
    total_area = pi * (diameter/2) ** 2
    print(f"The area of the patio is {total_area:.2f} square feet.")
    brick_l = 4/12
    brick_w = 6/12
    brick_area = brick_l * brick_w
    num_bricks = total_area/brick_area
    print(f"""The patio needs {ceil(num_bricks)} bricks (4" x 6" size).""")

patio_design()


def count_char_x(word: str, trgt_char: str) -> int:
    return sum([char == trgt_char for char in word])

count_char_x("California", "i")