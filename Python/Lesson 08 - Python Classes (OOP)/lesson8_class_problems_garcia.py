# In-Class Problems, Practice, and Notes

# # Animal Class Example
# class Animal():
#     num_instances = 0               # This variable is for the class itself, not objects
#     def __init__(self):
#         Animal.num_instances += 1
        
#     @classmethod                    # Decorator
#     def how_many_animals(cls):
#         print(cls.num_instances)    # Class

# milo = Animal()
# emilio = Animal()
# benji = Animal()
# blue = Animal()
# charlie = Animal()
# Animal.how_many_animals()
# print(Animal.num_instances)

# print(blue.num_instances)           # Objects also have access to class attributes
# blue.how_many_animals()             # Objects also have access to class methods

# blue.num_instances += 3             # Incrementing an object does not affect the class
# print(blue.num_instances)           # Now this is different
# Animal.how_many_animals()


# Pokemon instructor demonstration
import random as r

class Pokemon():
    # Attributes: species/pokedex number, health, level, speed, strength, defense, sp attack, sp def, types, moves, evolution requirements
    # Methods: attack, buffs, defend, evolve
    
    def __init__(self, name, species, gender):
        self.name = name
        self.species = species
        self.gender = gender
        self.health = r.randint(100, 200)
        self.level = r.randint(1, 10)
        self.speed = r.randint(50, 100)
        self.strength = r.randint(50,100)
        self.defense = r.randint(50,100)
        self.sp_attack = r.randint(50,100)
        self.sp_defense = r.randint(50,100)
        self.type = []
        self.moves = []
        self.evolution_requirements = []
    
    def level_up(self):
        self.level += 1
        self.health += r.randint(10, 20)
        self.speed += r.randint(5, 10)
        self.strength += r.randint(5,10)
        self.defense += r.randint(5,10)
        self.sp_attack += r.randint(5,10)
        self.sp_defense += r.randint(5,10)
        
        if all(self.evolution_requirements):
            self.evolve()
            
    def evolve(self):
        pass

    def attack(self, target: "Pokemon"):
        does_hit = False
        if self.speed > target.speed:
            does_hit = True
        elif self.speed < target.speed:
            does_hit = r.randint(1, 2) == 2
        
        multiplier = 1
        
        if does_hit:
            print('It hits!')
            
            # weakness/resistance check
            if True:
                multiplier = 2
                print("It's very effective!")
            
            target.health -= self.strength // 10
        else:
            print('It missed!')
            
        print(f"{target.name} has {target.health} health remaining.")
    
class Type():
    pass

class Trainer():
    pass


my_team = [Pokemon('bernie', 'Pikachu', 'M'), Pokemon('bernette', 'Pikachu', 'F')]

for pokemon in my_team:
    print(f"{pokemon.name}'s health and speed are {pokemon.health} and {pokemon.speed}")

# Levelup test
print('Leveling up {my_team[0].name}')
my_team[0].level_up()
print(f"{my_team[0].name}'s health and speed are {my_team[0].health} and {my_team[0].speed}")

# Attack test
print()
my_team[0].attack(my_team[1])
