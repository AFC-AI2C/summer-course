# #### Instructions:
# 1. Define a class `Planet` with an initializer that sets:
#    - `name`: planet’s name
#    - `coordinates`: the x, y, z coordinates of the planet
#    - `danger`: difficulty of completing missions  
#    - `resources`: reward value
#    - `atmosphere`: descriptive text

class Planet():
    def __init__(self, name:str, coordinates:tuple[float], danger:float, resources:float, atmosphere:str):
        self.name =name
        self.coordinates = coordinates
        self.danger =danger
        self.resources = resources
        self.atmosphere = atmosphere
#2. Override the `__str__` method to print a summary of the planet.

# by using __str__ "How should this object look when someone prints it, if you dont use it it will print with random memmory numbers

    def __str__(self)->str:

        return(
                f"Name: {self.name}\n"
                f"Coordinates: {self.coordinates}\n"
                f"Danger Level: {self.danger}\n"
                f"Resources: {self.resources}\n"
                f"Atmosphere: {self.atmosphere}\n"
                )

# 3. Override a built-in method to calculate the distance between two planets. (maybe `__sub__`?)

# buy using this __sub__ I can subtracts 2 plants from each other. 

    def __sub__(self, other)->float:
        if not isinstance(other, Planet):
            raise TypeError("Must only subtract Planet")
        
        x1, y1, z1 = self.coordinates
        x2, y2, z2 = other.coordinates

        return(
            (x1 - x2) ** 2 
            + (y1 - y2) ** 2 
            + (z1 - z2) **2
            )** (1/2)
    

planets = [ 
  Planet("Earth", (149.6, 0.0, 0.0), 0, 0, "Earth-like"),
  Planet("Mars", (227.9,   0.0,    1.0), 1, 20, "Thin"),
  Planet("Jupiter", (778.5,  50.0,   12.0), 3, 40, "Gas Giant"),
  Planet("Saturn", (1434.0, -80.0,  -20.0), 2, 35, "Gas Giant"),
  Planet("Uranus", (2871.0,  30.0,   40.0), 2, 45, "Icy"),
  Planet("Neptune", (4495.0, -25.0,   70.0), 4, 50, "Icy"),
  Planet("Pluto", (5906.0, 120.0,  -90.0), 5, 60, "Frozen"),
  Planet("Eris", (10100.0, 200.0, -130.0), 4, 55, "Frozen"),
  Planet("Kepler-22b", (600000.0,  0.0,   0.0), 3, 70, "Earth-like"),
  Planet("Proxima b", (402080.0, 30.0,  10.0), 5, 80, "Unknown")
]

for planet in planets:
    print(planet)


distances = (planets[0] - planets[2])
print(f"From: {planets[0].name} to {planets[2].name} is {distances:.02f} miles away")


