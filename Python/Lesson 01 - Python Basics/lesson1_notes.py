"""
name = input("What is your name? ")
favorite_number = int(input("What is your favorite number? "))
#print("Hello " + name)
#print("Your favorite number is " + str(favorite_number))
#print("Your favorite number minus 10 is " + str(favorite_number - 10))
print("Hello ", name)
print("Your favorite number is ", favorite_number)
print("Your favorite number minus 10 is ", favorite_number - 10)
"""

diameter_deal = input("What is the diameter for each small pizza? ")
area_small = 3.14 * (float(diameter_deal)/2) ** 2
area_deal = 2 * area_small
print(f"The amount of pizza in the deal as an area is {area_deal:.02f} square units.")
cost_deal = input("What is the cost of the 2 small pizza deal? ")
print(f"The cost per square unit of area of pizza in the deal is ${(float(cost_deal)/area_deal):.02f} per square unit.")

diameter_large = input("What is the diameter of the large pizza? ")
area_large = 3.14 * (float(diameter_large)/2) ** 2
print(f"The amount of area in the large pizza is {area_large:.02f} square units.")
cost_large = input("What is the cost of the large pizza? ")
print(f"The cost per square unit of area of large pizza is ${(float(cost_large)/area_large):.02f} per square unit.")

if (float(cost_large)/area_large) < (float(cost_deal)/area_deal):
    print("The large pizza is a better deal.")
elif (float(cost_large)/area_large) > (float(cost_deal)/area_deal):
    print("The two pizzas are a better deal.")
else:
    print("The pizzas are the same price.")