import math

class Spacecraft():
    def __init__(self, name: str, fuel_level: float, fuel_efficiency: float):
        self.name = name
        self.fuel_level = fuel_level
        self.fuel_efficiency = fuel_efficiency
        self.max_fuel = 200_000

    def add_fuel(self, amount: float) -> None:
        self.fuel_level = min(self.max_fuel, self.fuel_level + amount)
        self.fuel_level = max(self.fuel_level, 0)

    def calculate_required_fuel(self, distance: float) -> float:
        required_fuel = math.ceil(distance / self.fuel_efficiency)
        return required_fuel

    def check_fuel(self, distance: float) -> bool:
        if self.calculate_required_fuel(distance) <= self.fuel_level:
            return True
        else:
            return False

    def launch(self, distance: float) -> None:
        if self.check_fuel(distance):
            print('T minus... whatever, launch!')
            self.fuel_level -= self.calculate_required_fuel(distance)
            print(f"After this trip, spacecraft will have {self.fuel_level} liters of fuel remaining.")
        else:
            print('Not enough fuel to launch, sorry!')
        print(f"")

# Test run
if __name__ == "__main__":
    print()
    apollo26 = Spacecraft('Apollo 26', 1000, 100)
    print(apollo26.__dict__)
    print()
    apollo26.launch(50000)
    
    # run your tests here...