# ## 👨‍🚀 Player Class

# ### Purpose:
# Keeps track of the player’s progress, including visited planets, credits, fuel purchases, and mission completion.

# ### Instructions:
# 1. Define a class `Player` with an initializer that accepts:
#    - `name`: the player's name
#    - Optional: `difficulty`: affects starting credits and spacecraft

# 2. Track the following attributes:
#    - `current_planet`
#    - `distance_traveled`
#    - `visited_planets`
#    - `score`
#    - `credits`
#    - `mission_rewards`

# 3. Add methods to:
#    - Record visited planets and update distance and current planet
#    - Buy fuel for the spacecraft using available credits
#    - Calculate the player's score based off distance, credits, and mission rewards
#    - Display a status summary

# 4. Create a method to simulate a mission on the current planet with varying outcomes:
#    - Use danger level to calculate success chance
#    - Return success, partial, or fail outcomes with appropriate reward values
#    - Optional: limit the number of missions a player can do at a planet
from Avila_spacecraft_test  import Spacecraft
from Avila_plant_test import Planet, planets

class Player():
    def __init__(self, name, difficulty= "Normal"):
        self.name = name
        self.difficulty = difficulty


#these should all start with default values.

        self.current_planet = None
        self.distance_traveled = 0
        self.visited_planets = []
        self.score = 0
        self.mission_rewards = []
        self.spacecraft = None
        
        if difficulty == "Easy":
            self.credits = 1000
        elif difficulty == "Hard":
            self.credits = 200
        else:
            self.credits = 500

    def visit_planet(self, planet, distance):
        self.current_planet = planet
        self.visited_planets.append(planet)
        self.distance_traveled +=distance

player1 = Player("Gina")


player1.visit_planet(planets[0],150)

print(player1.name)
print(player1.current_planet)
print(player1.distance_traveled)
print(player1.visited_planets)




  