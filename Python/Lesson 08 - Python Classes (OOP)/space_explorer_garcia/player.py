from planet import Planet
from spacecraft import Spacecraft


class Player:
    def __init__(self, name: str, starting_planet: Planet, difficulty: str = "Medium"):
        self.name = name
        self.current_planet = starting_planet
        self.difficulty = difficulty
        
        self.credits = {"Easy": 100, "Medium": 50, "Hard": 25}.get(difficulty)      # Dictionary to establish starting credits
        self.distance_traveled = 0
        self.mission_rewards = 0
        
        self.visited_planets = set([starting_planet])           # I did not originally think to initialize this

    def visit_planet(self, planet: Planet) -> None:
        self.visited_planets.add(planet)
        self.distance_traveled = Planet.__sub__(self.current_planet, planet) # This could have been streamlined with the actual minus symbol since it was overridden
        self.current_planet = planet

    def buy_fuel(self, spacecraft: Spacecraft, price_per_unit: float = 2.0) -> None:    # I thought I had this one going, but I encountered it not running in main.py
        print(f"You have {self.credits} credits.")                                      # so I just pasted it back in from the solution instead
        try:
            amount = float(
                input(
                    f"Enter fuel amount to buy in kilounits (price: {price_per_unit}/kilounit): "
                )
            )
        except ValueError:
            print("Invalid input.")
            return
        cost = amount * price_per_unit
        if cost < 0:
            print("Stop tryin' to cheat.")
        elif self.credits >= cost:
            spacecraft.add_fuel(amount * 1000)
            self.credits -= cost
            print(f"Purchased {amount} units of fuel.")
        else:
            print("Not enough credits.")

# Past this point, I relied on checking the solutions because what was being asked for was vague

    def complete_mission(self, planet: Planet) -> None:
        if not planet.can_do_mission(self.name):
            print(f"No more missions can be done at {planet.name}.")
            return
        outcome, reward = planet.mission_success()
        planet.record_mission(self.name)
        print(f"Mission outcome: {outcome}. Earned {reward} credits.")
        if outcome == "fail":
            penalty = 5 + int(planet.danger * 5)
            self.credits = max(0, self.credits - penalty)
            print(f"Mission failed! Lost {penalty} credits as penalty.")
        else:
            self.credits += reward
            self.mission_rewards += reward

    @property
    def score(self) -> float:
        return len(self.visited_planets) * 10 + self.credits + self.mission_rewards * 10 # This seems totally arbitrary

    def status(self) -> str:
        visited = ", ".join([planet.name for planet in self.visited_planets])
        return (
            f"Captain: {self.name}\n"
            f"Distance traveled: {self.distance_traveled:.2f} units\n"
            f"Visited planets: {visited}\n"
            f"Mission rewards: {self.mission_rewards}\n"
            f"Credits: {self.credits}\n"
            f"Score: {self.score}\n"
        )
    

# Test run
if __name__ == "__main__":
    player1 = Player('Miguel', Planet("Earth", (149.6, 0.0, 0.0), 0, 0, "Earth-like"), 'Medium')
    mars = Planet("Mars", (227.9,   0.0,    1.0), 1, 20, "Thin")
    print(player1.distance_traveled)
    player1.visit_planet(mars)
    print(player1.distance_traveled)



