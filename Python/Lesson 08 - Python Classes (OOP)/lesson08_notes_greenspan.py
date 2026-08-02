import math  # Supports math.dist() for coordinates.
# Python 3.7 (via PEP 557) introduced dataclasses as a standard library.
from dataclasses import dataclass, field, InitVar

#from typing import Literal  #Implements type hinting with specific string values.
#allow_resources = Literal['crystal', 'gas']  #Implements type hinting with specific string values.
#from enum import Enum       #  #Implements type hinting with dynamic values.

### Delete if not necessary.
### Implements Dictionary Mapping + Data Class.
### Instead of creating separate variable names like earth = Planet(...),
### store them ina dictionary keyed by their name.
### Using dataclaseses makes defining the Planet structure clean and readable.

@dataclass
class Spacecraft():
    """Manages travel between planets, including tracking fuel and launching to destinations."""

    name: str
    fuel_efficiency: int
    max_fuel: int = 200_000
    # Assigns fuel_level as a mutable variable using initial_fuel_level as an initial argument. 
    initial_fuel_level: InitVar[int]
    fuel_level: int = field(init=False)

    def __post_init__(self, name, initial_fuel_level: int):
        self.fuel_level = initial_fuel_level

    def add_fuel(self, amount):
        self.fuel_level += amount
        #self.fuel_level = min(self.fuel_level, self.fuel_level + amount)
        #self.fuel_level = max(self.fuel_level, 0)

    def calc_fuel(self, distance):
        return distance / self.fuel_efficiency

    def has_enough_fuel(self, distance):
#        return self.fuel_level >= self.calc_fuel(distance)     #one-liner
        if self.fuel_level >= self.calc_fuel(distance):
#            print(f"{self.name} has enough fuel. \t | Fuel Needed: {self.calc_fuel(distance)} \t Fuel Level: {self.fuel_level}")
            return True
        else:
#            print(f"{self.name} does not have enough fuel. \t | Fuel Needed: {self.calc_fuel(distance)} \t Fuel Level: {self.fuel_level}")
            return False

    def launch(self, distance):
        if self.has_enough_fuel(distance):
            self.fuel_level -= self.calc_fuel(distance)
            print(f"{self._name} launched successfully and completed the journey.")
        else:
            print(f"FUEL WARNING: Launch aborted. Fuel Level: {self.fuel_level} \t Fuel Needed: {self.calc_fuel(distance)}")

if __name__ == '__main__':
    my_ship = Spacecraft("McQueen's Motorcycle", 100, 5)
    my_ship.has_enough_fuel(1000)
    my_ship.launch(1000)
    my_ship.add_fuel(100)
    my_ship.launch(1000)

@dataclass
class Planet:
    """There are a variety of planets in this system. Some of the planets are discovered, but many are not. 
    The planets have a number of resources and can be of varying danger levels. 
    Add some descriptive text to the planet to make them feel more alive.
    """

    name: str
    coordinates: tuple[float, float, float]
    danger: int
    resources: int
    atmosphere: str

    # Comment out the definition of __str__ to use @dataclass method instead.    
    # def __str__(self):
    #     return f'{self.name}, located at {self.coordinates}, is a planet with {self.danger} danger, {self.resources} resources, and {self.atmosphere} atmosphere.'

    def __sub__(self, operand: 'Planet'):
        if not isinstance(operand, Planet):
            raise TypeError('Must only subtract planets')
#        distance = sum([(c1-c2)**2 for c1,c2 in zip(self.coordinates, operand.coordinates)]) ** (1/2)
#        return distance
        return math.dist(self.coordinates, operand.coordinates)  #Replace the previous 2 lines using math.dist() function.

# Tests the Planet class.
# if __name__ == '__main__':
#     planets = [
#         Planet("Earth", (149.6, 0.0, 0.0), 0, 0, "Earth-like"),
#         Planet("Mars", (227.9,   0.0,    1.0), 1, 20, "Thin"),
#         Planet("Jupiter", (778.5,  50.0,   12.0), 3, 40, "Gas Giant"),
#         Planet("Saturn", (1434.0, -80.0,  -20.0), 2, 35, "Gas Giant"),
#         Planet("Uranus", (2871.0,  30.0,   40.0), 2, 45, "Icy"),
#         Planet("Neptune", (4495.0, -25.0,   70.0), 4, 50, "Icy"),
#         Planet("Pluto", (5906.0, 120.0,  -90.0), 5, 60, "Frozen"),
#         Planet("Eris", (10100.0, 200.0, -130.0), 4, 55, "Frozen"),
#         Planet("Kepler-22b", (600000.0,  0.0,   0.0), 3, 70, "Earth-like"),
#         Planet("Proxima b", (402080.0, 30.0,  10.0), 5, 80, "Unknown")
#     ]
#     print(f'The distance between {planets[0].name} and {planets[1].name} is {planets[0] - planets[1]}.')
#Test TypeError when subtracting planets.
#   planets[0] - 5

@dataclass
class Player():
    """The player should keep track of which planets have been visited, how many credits they have, 
    and have the ability to complete missions on the planet they're currently at. 
    The player can also purchase fuel for their spacecraft when they are on a planet.
    """

    name: str
    difficulty: int = 3  #  #Initialize parameter with default. Affects starting credits and spacecraft.
    spacecraft: Spacecraft = field(init=False)
    _current_planet: Planet = field(init=False, default_factory=lambda: Planet(
            "Earth", (149.6, 0.0, 0.0), 0, 0, "Earth-like"
            )
    _visited_planets: set[str] = field(
            init=False, default_factory=lambda: {"Earth"}
            )
    _score: int = field(init=False, default=0)
    _credits: int = field(init=False, default=0)
    _mission_rewards: list = field(init=False, default_factory=list)

  def __post_init__(self):
    # Calculate spacecraft settings based on difficulty.
    if self.difficulty == 1:
        initial_fuel_level = 120
        fuel_efficiency = 1.2
    elif self.difficulty == 2:
        initial_fuel_level = 110
        fuel_efficiency = 1.1
    elif self.difficulty == 3:
        initial_fuel_level = 100
        fuel_efficiency = 1
    elif self.difficulty == 4:
        initial_fuel_level = 90
        fuel_efficiency = 0.9
    elif self.difficulty == 5:
        initial_fuel_level = 80
        fuel_efficiency = 0.8

    self.spacecraft = Spacecraft(self.name, initial_fuel_level, fuel_efficiency)
    self._credits = 500 * (5 - self.difficulty)

    def planet_update(self, destination: 'Planet'):
        self._current_planet = destination
        self._visited_planets.union(destination)
        
    def purchase_fuel(self, cost):
        self._credits -= cost
        self.spacecraft.add_fuel(cost/1)

    def complete_mission(self, planet: Planet):
        self._planet_visited.append(planet.name)
        self._credits += planet.resources
        self._mission_rewards += None  #Update mission rewards.

# planets_available = [
#     Planet("Earth", (149.6, 0.0, 0.0), 0, 0, "Earth-like"),
#     Planet("Mars", (227.9,   0.0,    1.0), 1, 20, "Thin"),
#     Planet("Jupiter", (778.5,  50.0,   12.0), 3, 40, "Gas Giant"),
#     Planet("Saturn", (1434.0, -80.0,  -20.0), 2, 35, "Gas Giant"),
#     Planet("Uranus", (2871.0,  30.0,   40.0), 2, 45, "Icy"),
#     Planet("Neptune", (4495.0, -25.0,   70.0), 4, 50, "Icy"),
#     Planet("Pluto", (5906.0, 120.0,  -90.0), 5, 60, "Frozen"),
#     Planet("Eris", (10100.0, 200.0, -130.0), 4, 55, "Frozen"),
#     Planet("Kepler-22b", (600000.0,  0.0,   0.0), 3, 70, "Earth-like"),
#     Planet("Proxima b", (402080.0, 30.0,  10.0), 5, 80, "Unknown")
# ]


# Raw planet data: easy to add, edit, or import.
raw_planet_data = [
    ("Earth", (149.6, 0.0, 0.0), 0, 0, "Earth-like"),
    ("Mars", (227.9,   0.0,    1.0), 1, 20, "Thin"),
    ("Jupiter", (778.5,  50.0,   12.0), 3, 40, "Gas Giant"),
    ("Saturn", (1434.0, -80.0,  -20.0), 2, 35, "Gas Giant"),
    ("Uranus", (2871.0,  30.0,   40.0), 2, 45, "Icy"),
    ("Neptune", (4495.0, -25.0,   70.0), 4, 50, "Icy"),
    ("Pluto", (5906.0, 120.0,  -90.0), 5, 60, "Frozen"),
    ("Eris", (10100.0, 200.0, -130.0), 4, 55, "Frozen"),
    ("Kepler-22b", (600000.0,  0.0,   0.0), 3, 70, "Earth-like"),
    ("Proxima b", (402080.0, 30.0,  10.0), 5, 80, "Unknown")
]

if __name__ == '__main__':
    print(f'The distance between {planets[0].name} and {planets[1].name} is {planets[0] - planets[1]}.')