# prompt user for value
diameter_str = input("Please enter the diameter: ")

# convert to float
diameter_float = float(diameter_str)

# area = pi * r ** 2
area_float = 3.14 * (diameter_float / 2) ** 2

print("The area is " + str(area_float))