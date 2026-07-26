from area import rectangle_area, circle_area, tri_area

rectangle_area(10,10)
circle_area(10)
tri_area(10,10)


passenger_list = ["Lopez", "Chen", "Okafor", "Smith", "Patel"]

for index, passenger in enumerate(passenger_list, 1):
    print(f"Passenger {passenger} in seat {index}")

