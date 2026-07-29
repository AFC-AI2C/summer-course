import random
import math

class Planet:
    def __init__(
        self,
        name: str,
        coordinates: tuple[float, float, float],
        danger: float,
        resources: float,
        atmosphere: str,
    ):
        self.name = name
        self.coordinates = coordinates
        self.danger = danger
        self.resources = resources
        self.atmosphere = atmosphere

        # Maximum missions allowed: fewer for higher danger... had to get this part from solutions, because I didn't know what the instructions meant
        self.max_missions = max(1, 4 - int(self.danger))
        self.missions_done: dict[str, int] = {}

    def __str__(self) -> str:
        return (f"""
              Planet: {self.name}
              Coordinates: {self.coordinates}
              Danger Level: {self.danger}
              Resources: {self.resources}
              Atmosphere: {self.atmosphere}
              """)

    def __sub__(self, other) -> float:
        # calculate the distance between this planet object (self) and another planet object (other)
        # I reused code from lesson 7 in-class problems
        root = 0
        for value in range(len(self.coordinates)):
            root += (other.coordinates[value] - self.coordinates[value]) ** 2
        return math.sqrt(root)

# After this point, I really had to look at the provided solution, because the instructions are pretty vague on what is even being asked

    def can_do_mission(self, player_name) -> bool:
        if self.missions_done.get(player_name, 0) < self.max_missions:          # .get() because missions_done is a dictionary, must be populated by Player class...
            return True
        else:
            return False

    def record_mission(self, player_name: str) -> None:
        self.missions_done[player_name] = self.missions_done.get(player_name, 0) + 1

    def mission_success(self) -> tuple[str, float]:
        chance = max(0.4, 1.0 - 0.15 * self.danger)
        roll = random.random()
        if roll < chance:
            return "success", self.resources
        elif roll < chance + 0.4:
            return "partial", self.resources // 2
        else:
            return "fail", 0


# Test run
if __name__ == "__main__":
    earth = Planet("Earth", (149.6, 0.0, 0.0), 0, 0, "Earth-like")
    mars = Planet("Mars", (227.9,   0.0,    1.0), 1, 20, "Thin")
    jupiter =Planet("Jupiter", (778.5,  50.0,   12.0), 3, 40, "Gas Giant")
    saturn = Planet("Saturn", (1434.0, -80.0,  -20.0), 2, 35, "Gas Giant")
    uranus = Planet("Uranus", (2871.0,  30.0,   40.0), 2, 45, "Icy")
    neptune = Planet("Neptune", (4495.0, -25.0,   70.0), 4, 50, "Icy")
    pluto = Planet("Pluto", (5906.0, 120.0,  -90.0), 5, 60, "Frozen")
    eris = Planet("Eris", (10100.0, 200.0, -130.0), 4, 55, "Frozen")
    kepler = Planet("Kepler-22b", (600000.0,  0.0,   0.0), 3, 70, "Earth-like")
    proxima = Planet("Proxima b", (402080.0, 30.0,  10.0), 5, 80, "Unknown")

    print(earth)
    print(earth - mars)





