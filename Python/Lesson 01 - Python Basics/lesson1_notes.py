"""
These notes solve the in class exercises.
"""

def name_num_att1() -> None: 
    """Simple input: 
        Asks the user for their name
        Asks the user for their favorite number
        Prints “Hello” and then their name
        Prints “Your favorite number is” and then their favorite number
        Prints “Your favorite number minus 10 is” their favorite number minus 10
    """
    name = input("What is your name? ")
    favorite_number = int(input("What is your favorite number? "))
    #print("Hello " + name)
    #print("Your favorite number is " + str(favorite_number))
    #print("Your favorite number minus 10 is " + str(favorite_number - 10))
    print("Hello", name)
    print("Your favorite number is", favorite_number)
    print("Your favorite number minus 10 is", favorite_number - 10)
    

def name_num1_att2() -> None:
    """Simple input: 
        Asks the user for their name
        Asks the user for their favorite number
        Prints “Hello” and then their name
        Prints “Your favorite number is” and then their favorite number
        Prints “Your favorite number minus 10 is” their favorite number minus 10
    """
    name = input("What is your name? ")
    while True:
        favorite_number = input("What is your favorite number? ")
        try:
            favorite_number = int(favorite_number)
            break
        except:
            print("Please choose an integer. You may try again.")
    print("Hello", name)
    print("Your favorite number is", favorite_number)
    print("Your favorite number minus 10 is", favorite_number - 10)

def pizza_deal_att1() -> None:
    """prompts the user for a diameter of the pizza and outputs the area
        Stretch goal #1:  calculates the price per area.  The user should input the diameter and the cost.
        Stretch goal #2:  calculates the best deal.  
            The user should input three diameters (two for the first deal, one for the second deal), and the two costs.
    """
    while True:
        diameter_deal = input("What is the diameter for each small pizza? ")
        try:
            diameter_deal = float(diameter_deal)
            break
        except:
            print("Please input a real number. You may try again.")
    area_small = 3.14 * (diameter_deal/2) ** 2
    area_deal = 2 * area_small
    print(f"The amount of pizza in the deal as an area is {area_deal:.1f} square units.")
    while True:
        cost_deal = input("What is the cost of the 2 small pizza deal? ")
        try:
            cost_deal = float(cost_deal)
            break
        except:
            print("Please input a real number. You may try again.")
    print(f"The cost per square unit of area of pizza in the deal is ${cost_deal/area_deal:.02f} per square unit.")

    while True:
        diameter_large = input("What is the diameter of the large pizza? ")
        try:
            diameter_large = float(diameter_large)
            break
        except:
            print("Please input a real number. You may try again.")
    area_large = 3.14 * (diameter_large/2) ** 2
    print(f"The amount of area in the large pizza is {area_large:.1f} square units.")
    while True:
        cost_large = input("What is the cost of the large pizza? ")
        try:
            cost_large = float(cost_large)
            break
        except:
            print("Please input a real number. You may try again.")    
    print(f"The cost per square unit of area of large pizza is ${cost_large/area_large:.02f} per square unit.")

    if (cost_large/area_large) < (cost_deal/area_deal):
        print("The large pizza is a better deal.")
    elif (cost_large/area_large) > (cost_deal/area_deal):
        print("The two pizzas are a better deal.")
    else:
        print("The pizzas are the same price.")

if __name__ == "__main__":
    name_num1_att2()
    pizza_deal_att1() 