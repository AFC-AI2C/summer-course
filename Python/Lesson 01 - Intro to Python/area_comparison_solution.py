# pizza one
diameter_one_str = input("Please enter the diameter for deal 1, pizza 1: ")
diameter_one_float = float(diameter_one_str)
area_one_float = 3.14 * (diameter_one_float / 2) ** 2

print("The area for pizza one is " + str(area_one_float))

# pizza two
diameter_two_str = input("Please enter the diameter for deal 1, pizza 2: ")
diameter_two_float = float(diameter_two_str)
area_two_float = 3.14 * (diameter_two_float / 2) ** 2

print("The area for pizza two is " + str(area_two_float))

price_str = input("Please enter the cost for deal 1: $")
price_float = float(price_str)

# cost per area = cost / total area
cost_per_area_one = price_float / (area_one_float + area_two_float)

print("The cost per area for deal one is " + str(cost_per_area_one))


# other deal
diameter_str = input("Please enter the diameter for deal 2: ")

# convert to float
diameter_float = float(diameter_str)

# area = pi * r ** 2
area_float = 3.14 * (diameter_float / 2) ** 2

print("The area is " + str(area_float))

price_str = input("Please enter the cost for deal 2: $")
price_float = float(price_str)

# cost per area = cost / area
cost_per_area_two = price_float / area_float

print("The cost per area is " + str(cost_per_area_two))

print("Deal one cost per area:  " + str(cost_per_area_one))
print("Deal two cost per area:  " + str(cost_per_area_two))
print("The lower number is better!")