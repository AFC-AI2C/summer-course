p_dia = float(input("What is the diameter of your pizza in inches? "))
pi = 3.14
p_area = pi * (p_dia/2)**2
p_cost = float(input("What is the cost of your pizza in dollars? "))
p_area_cost = p_cost/p_area


print(f"Your pizza diameter is {p_dia} inches.")
print(f"Your pizza area is {p_area} square inches.")
print(f"Your pizza costs ${p_cost:.02f}.")
print(f"Your pizza costs ${p_area_cost:.04f} dollars per square inch.")