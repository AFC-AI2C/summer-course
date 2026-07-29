#space explorer
class Spacecraft():
    def __init__(self, name, fuel_level, fuel_efficiency):
        self._name = name
        self._fuel_level = fuel_level
        self._fuel_efficiency = fuel_efficiency
        #self.max_fuel = 200_000

    def add_fuel(self, amount):
        self._fuel_level += amount
        #self._fuel_level = min(self._fuel_level, self._fuel_level + amount)
        #self._fuel_level = max(self._fuel_level, 0)

    def calc_fuel(self, distance):
        return distance / self._fuel_efficiency

    def has_enough_fuel(self, distance):
#        return self._fuel_level >= self.calc_fuel(distance)     #one-liner
        if self._fuel_level >= self.calc_fuel(distance):
#            print(f"{self.name} has enough fuel. \t | Fuel Needed: {self.calc_fuel(distance)} \t Fuel Level: {self.fuel_level}")
            return True
        else:
#            print(f"{self.name} does not have enough fuel. \t | Fuel Needed: {self.calc_fuel(distance)} \t Fuel Level: {self.fuel_level}")
            return False

    def launch(self, distance):
        if self.has_enough_fuel(distance):
            self._fuel_level -= self.calc_fuel(distance)
            print(f"{self._name} launched successfully and completed the journey.")
        else:
            print(f"Fuel Warning for {self._name} | Fuel Needed: {self.calc_fuel(distance)} \t Fuel Level: {self._fuel_level} \t Add fuel before launch.")

if __name__ == '__main__':
    my_ship = Spacecraft("McQueen's Motorcycle", 100, 5)
    my_ship.has_enough_fuel(1000)
    my_ship.launch(1000)
    my_ship.add_fuel(100)
    my_ship.launch(1000)


#hands on 2
#planet class
#from typing import Literal
#allow_resources = Literal['crystal', 'gas']
#from enum import Enum       #include for dynamic type hinting
class Planet():
    def __init__(self, name: str, coordinates: tuple[int, int, int], danger: int, resources: int, atmosphere: str):
        self.name = name
        self.coordinates = coordinates
        self.danger = danger
        self.resources = resources
        self.atmosphere = atmosphere
    def __str__(self):
        return f'{self.name}, located at {self.coordinates}, is a planet with {self.danger} danger, {self.resources} resources, and {self.atmosphere} atmosphere.'
    def __sub__(self, operand: 'Planet'):
        if not isinstance(operand, Planet):
            raise TypeError('Must only subtract planets')
#        (x1,y1,z1), (x2,y2,z2) = self.coordinates, operand.coordinates
#        distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
        distance = sum([(c1-c2)**2 for c1,c2 in zip(self.coordinates, operand.coordinates)]) ** (1/2)
        return distance

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

if __name__ == '__main__':
    print(f'The distance between {planets[0].name} and {planets[1].name} is {planets[0] - planets[1]}.')