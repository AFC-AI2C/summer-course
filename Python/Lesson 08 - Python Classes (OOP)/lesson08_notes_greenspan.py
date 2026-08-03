import math  # Supports math.dist() for coordinates.
import random

class Spacecraft():
    """Manages travel between planets, including tracking fuel and launching to destinations."""

    def __init__(self, name, fuel_level, fuel_efficiency):
        self.name = name
        self.fuel_level = fuel_level
        self.max_fuel = 200_000
        self.fuel_efficiency = fuel_efficiency

    def add_fuel(self, amount):
        self.fuel_level += amount 

    def calc_fuel(self, distance):
        return distance / self.fuel_efficiency

    def has_enough_fuel(self, distance):
#        return self.fuel_level >= self.calc_fuel(distance)     #one-liner
        if self.fuel_level >= self.calc_fuel(distance):
            return True
        else:
            return False

    def launch(self, current_planet, destination, player: 'Player'):
        if destination.name == current_planet.name:
            print(f"{self.name} is already at {destination.name}.")
            return None
        distance = current_planet - destination
        if self.has_enough_fuel(distance):
            self.fuel_level -= self.calc_fuel(distance)
            print(f"Welcome to {destination.name}.")
            player.planet_update(destination)
        else:
            print(f"INSUFFICIENT FUEL -- Distance: {distance} \t Fuel Needed: {self.calc_fuel(distance)} \t Fuel Level: {self.fuel_level}")

    def __str__(self):
        return f"{{'Name': {self.name}, 'Fuel Level': {self.fuel_level}, 'Fuel Efficiency': {self.fuel_efficiency}}}"


class Planet:
    """There are a variety of planets in this system. Some of the planets are discovered, but many are not. 
    The planets have a number of resources and can be of varying danger levels. 
    Add some descriptive text to the planet to make them feel more alive.
    """

    def __init__(self, name, coordinates, danger, resources, atmosphere):
        self.name = name
        self.coordinates = coordinates
        self.danger = danger
        self.resources = resources
        self.atmosphere = atmosphere

    def __str__(self):
        return f"{{'Name': {self.name}, 'Location': {self.coordinates}, 'Danger': {self.danger}, 'Resources': {self.resources}, 'Atmosphere': {self.atmosphere}}}"

    def __sub__(self, operand: 'Planet'):
        if not isinstance(operand, Planet):
            raise TypeError('Must only subtract planets')
        return math.dist(self.coordinates, operand.coordinates) 


class Player():
    """The player should keep track of which planets have been visited, how many credits they have, 
    and have the ability to complete missions on the planet they're currently at. 
    The player can also purchase fuel for their spacecraft when they are on a planet.
    """

    def __init__(self, spacecraft_choice, difficulty=3):
        if spacecraft_choice == 1:
            name, fuel_level_input, fuel_efficiency_input = ("Vostok 1", 250, 1.5)
        elif spacecraft_choice == 2:
            name, fuel_level_input, fuel_efficiency_input = ("Voyager 1", 400, 2.0)
        elif spacecraft_choice == 3:
            name, fuel_level_input, fuel_efficiency_input = ("Apollo 11", 600, 2.5)
        self.name = name
        self.difficulty = difficulty
        if self.difficulty == 1:
            initial_fuel_multiplier = 1.2
        elif self.difficulty == 2:
            initial_fuel_multiplier = 1.1
        elif self.difficulty == 3:
            initial_fuel_multiplier = 1.0
        elif self.difficulty == 4:
            initial_fuel_multiplier = 0.9
        elif self.difficulty == 5:
            initial_fuel_multiplier = 0.8
        self.spacecraft = Spacecraft(self.name, fuel_level_input * initial_fuel_multiplier, fuel_efficiency_input)
        self.credits = 500 + (5 - difficulty + 1) * 100
        self.current_planet = Planet(
            "Earth", (149.6, 0.0, 0.0), 0, 0, "Earth-like"
            )
        self.visited_planets = {"Earth"}
        self.score = 0 

    def planet_update(self, destination: 'Planet'):
        self.current_planet = destination
        self.visited_planets.union(destination.name)
        
    def purchase_fuel(self, cost):
        if self.credits >= cost:
            self.credits -= cost
            self.spacecraft.add_fuel(cost)
        else:
            print(f"You only have {self.credits} credits.")

    def calculate_score(self):
        # Calculate the player's score based off distance, credits, and mission rewards. 
        pass

    def status_summary(self):
        spacecraft_summary = self.spacecraft.__str__()
#        "{{'Name': {self.name}, 'Fuel Level': {self.fuel_level}, 'Fuel Efficiency': {self.fuel_efficiency}}}"
        planet_summary = self.current_planet.__str__()
#        "{{'Name': {self.name}, 'Location': {self.coordinates}, 'Danger': {self.danger}, 'Resources': {self.resources}, 'Atmosphere': {self.atmosphere}}}"
        player_summary = f"{{'Credits': {self.credits}, 'Visited Planets': {self.visited_planets}, 'Score': {self.score}}}"
        print(spacecraft_summary)
        print(planet_summary)
        print(player_summary)

    def simulate_mission(self):
        #TO DO: Implement option to limit the number of missions a player can do at a planet.
        p_success = (6 - self.current_planet.danger) / 5
        if random.random() < p_success:
            print(f"MISSION SUCCESS: +{self.current_planet.resources} credits!")
            self.credits += self.current_planet.resources 
        elif random.randint(0,1):
            print(f"PARTIAL SUCCESS: +{math.floor(0.67 * self.current_planet.resources)} credits!")
            self.credits += math.floor(0.67 * self.current_planet.resources)
        else:
            print("MISSION FAILURE: +0 credits")

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

# raw_planet_data = [
#     ("Earth", (149.6, 0.0, 0.0), 0, 0, "Earth-like"),
#     ("Mars", (227.9,   0.0,    1.0), 1, 20, "Thin"),
#     ("Jupiter", (778.5,  50.0,   12.0), 3, 40, "Gas Giant"),
#     ("Saturn", (1434.0, -80.0,  -20.0), 2, 35, "Gas Giant"),
#     ("Uranus", (2871.0,  30.0,   40.0), 2, 45, "Icy"),
#     ("Neptune", (4495.0, -25.0,   70.0), 4, 50, "Icy"),
#     ("Pluto", (5906.0, 120.0,  -90.0), 5, 60, "Frozen"),
#     ("Eris", (10100.0, 200.0, -130.0), 4, 55, "Frozen"),
#     ("Kepler-22b", (600000.0,  0.0,   0.0), 3, 70, "Earth-like"),
#     ("Proxima b", (402080.0, 30.0,  10.0), 5, 80, "Unknown")
# ]


def test_planet():
    print(f'The distance between {planets[0].name} and {planets[1].name} is {math.ceil(planets[0] - planets[1])}.')
    #Test TypeError when subtracting planets.
    try:
        planets[0] - 5
    except TypeError as e:
        print(e)

def test_player():
    print('# \t Spacecraft \t Fuel Level \t Fuel Efficiency')
    print('1 \t Vostok 1 \t 250 \t\t 1.5')
    print('2 \t Voyager 1 \t 400 \t\t 2.0')
    print('3 \t Apollo 11 \t 600 \t\t 2.5')
    spacecraft_choice = int(input("Choose a spacecraft (1, 2, or 3): "))
    gamer = Player(spacecraft_choice=3, difficulty=3)
    print(gamer.status_summary())

def test_spacecraft():
    my_ship = Spacecraft("Voyager 1", 100, 2.0)
    print(my_ship.has_enough_fuel(planets[0] - planets[1]))
    my_ship.launch(planets[0], planets[8], gamer)
    my_ship.add_fuel(100)
    my_ship.launch(planets[0], planets[1], gamer)

# if __name__ == '__main__':
#     test_planet()
#     test_player()
#     test_spacecraft()

# Performs the main loop to play the game.
print('# \t Spacecraft \t Fuel Level \t Fuel Efficiency')
print('1 \t Vostok 1 \t 250 \t\t 1.5')
print('2 \t Voyager 1 \t 400 \t\t 2.0')
print('3 \t Apollo 11 \t 600 \t\t 2.5')
spacecraft_choice = int(input("Choose a spacecraft (1, 2, or 3): "))
gamer = Player(spacecraft_choice=3, difficulty=3)
while True:
    print("# \t Options")
    print("1 \t View Summary")
    print("2 \t Attempt Mission")
    print("3 \t Add Fuel")
    print("4 \t Launch")
    action = int(input("Choose an option (1, 2, 3, or 4): "))
    if action == 1:
        gamer.status_summary()
    elif action == 2:
        gamer.simulate_mission()
    elif action == 3:
        amount = int(input(f"Enter amount of fuel to add (whole number between 1 and {gamer.spacecraft.fuel_level}): "))
        gamer.purchase_fuel(amount)
    elif action == 4:
        for idx, planet in enumerate(planets, 1):
            print(idx, "\t", planet)
        destination = int(input(f"Choose a destination (1, 2, ..., 10): "))
        gamer.spacecraft.launch(gamer.current_planet, planets[destination-1], gamer) 






