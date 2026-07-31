class Spacecraft():
    def __init__(self, name:str, fuel_level:float,fuel_efficiency:float):
        self.name = name 
        self.fuel_level = fuel_level
        self.fuel_efficiency = fuel_efficiency
        self.max_fuel = 200_000

# makes it print right 

    def __str__(self) ->str:
        return (
            f"Name: {self.name}, "
            f"Fuel Level: {self.fuel_level}, " 
            f"Fuel Efficiency {self.fuel_efficiency}") 

#   - Add Fuel
    def add_fuel(self, amount_fuel):
        self.fuel_level = min(self.max_fuel, self.fuel_level + amount_fuel)
        self.fuel_level = max(self.fuel_level, 0)

#    - Calculate the fuel required for a given distance
    def calculate_needed_fuel(self, distance):
        amount = distance /self.fuel_efficiency
        return amount

#    - Check if enough fuel is available to travel that distance
    def fuel_check(self,distance):
        fuel_check1 = self.fuel_level >= self.calculate_needed_fuel(distance)
        return fuel_check1
    


#    - Launch the spacecraft and deduct fuel if successful
    def launch(self,distance):
        if self.fuel_check(distance):
            self.fuel_level -= self.calculate_needed_fuel(distance) 
            print(f'You were able to launch {self.name} {distance} miles with fuel reamining {self.fuel_level:.02f} gallons')

        else:
            print(
            f"Not enough fuel to launch"
            f"fuel needed to go: {self.calculate_needed_fuel(distance):.02f}"
            f'you only have: {self.fuel_level:.02f}'
            )
   

spacecrafts = [
   Spacecraft("Vostok 1", 250, 1.5),
   Spacecraft("Voyager 1", 400, 2.0),
   Spacecraft("Apollo 11", 600, 2.5) 
]       


for spacecraft in spacecrafts:
        print(spacecraft)

spacecrafts[0].launch(100)

