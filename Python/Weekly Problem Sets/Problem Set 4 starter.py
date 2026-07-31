# problem 1
class Soldier:
    """Represents a soldier with rank, fitness, and deployment status."""

    def __init__(self, name: str, rank: str, fitness: int, deployed: bool):
        self.name = name
        self.rank = rank
        self.fitness = fitness
        self.deployed = deployed

    def dispatch(self) -> None:
        """Mark this soldier as deployed."""
        self.deployed = True

    def __str__(self) -> str:
        return f"{self.name} ({self.rank}), fitness: {self.fitness}, deployed: {self.deployed})"


def process_reports(report_list: list[str]) -> tuple[dict[str, Soldier], set[str]]:
    """Parse report strings and return (roster_dict, ranks_set)."""
    
    roster = {}
    unique_ranks = []
    
    for string in report_list:
        
        # I adjusted from .strip() to .replace() in some cases
        string_processing = string.replace("Fitness:", "")
        string_processing = string_processing.replace("Status:", "")
        string_processing = string_processing.replace(" ", "")
        string_list = string_processing.split("|")
                                        
        dep_status = False
        if string_list[3].lower() == 'deployed':
            dep_status = True
        
        soldier_name = string_list[0].title()
        soldier_obj = Soldier(soldier_name, string_list[1].upper(), int(string_list[2]), dep_status)
        roster[soldier_name] = soldier_obj
        
        if soldier_obj.rank not in unique_ranks:
            unique_ranks.append(soldier_obj.rank)
    
    unique_ranks = set(unique_ranks)
    
    return roster, unique_ranks


def show_available(roster: dict[str, Soldier]) -> None:
    """Display all available soldiers, sorted alphabetically."""
    
    available_list = []
    
    for soldier_object in roster.values():
        if soldier_object.deployed == False:
            available_list.append(soldier_object.name)
    
    available_list.sort()
    
    print(f"Available soldiers: {available_list}")
        


def dispatch(roster: dict[str, Soldier], name: str) -> None:
    """Dispatch a soldier by name, or print an error if not available."""
    
    titled_name = name.title()
       
    try:
        global updated_status_list
        updated_status_list.append(titled_name)
    except:
        updated_status_list = [titled_name]
    
    if titled_name not in roster:
        print(f"{titled_name} not found in roster.")
    elif roster[titled_name].deployed == True:
        print(f"Dispatching {titled_name}...\t{titled_name} is already deployed.")
    else:
        roster[titled_name].deployed = True
        print(f"Dispatching {titled_name}...\tDone. Status set to deployed.")


def fitness_report(roster: dict[str, Soldier]) -> dict[str, list[str]]:
    """Return a dict with 'high', 'medium', 'low' fitness bands."""
    high_band = []
    medium_band = []
    low_band = []
    fitness_roster = {}
    
    for soldier_obj in roster.values():
        if soldier_obj.fitness < 60:
            low_band.append(soldier_obj.name)
        elif soldier_obj.fitness < 80:
            medium_band.append(soldier_obj.name)
        else:
            high_band.append(soldier_obj.name)

    fitness_roster['high'] = sorted(high_band)
    fitness_roster['medium'] = sorted(medium_band)
    fitness_roster['low'] = sorted(low_band)
    
    return fitness_roster


# Given initial "reports" as raw strings
reports = [
    "SANTOS | Private | Fitness:91 | Status:available",
    "KOWALSKI | Corporal | Fitness:74 | Status:deployed",
    "OKAFOR | Sergeant | Fitness:88 | Status:available",
    "BRIGGS | Private | Fitness:55 | Status:available",
    "NAKAMURA | Corporal | Fitness:82 | Status:deployed",
    "REYES | Sergeant | Fitness:79 | Status:available",
]


# # My original testing section for problem 1:
# if __name__ == "__main__":

#     # Produce initial outputs
#     roster, ranks = process_reports(reports)
#     fitness_roster = fitness_report(roster)

#     # Print with formatting
#     print(f"""
# === ROSTER LOADED ===
# {len(roster)} soldiers on record.
# Ranks on file: {ranks}
# """)

#     show_available(roster)

#     print()
#     dispatch(roster, 'santos')
#     dispatch(roster, 'kowalski')

#     print('\nUpdated Status:')

#     for soldier in updated_status_list:
#         print(f"\t{soldier:8}: {'deployed' if roster[soldier].deployed else 'available'}")

#     print("\nFitness report:")
#     fitness_roster = fitness_report(roster)
#     for pt_band in fitness_roster:
#         print(f"  {pt_band:6}: {fitness_roster[pt_band]}")

#     print()
    
    
    
# problem 2
class Recipe:
    """Represents a recipe with a name and list of ingredients."""

    def __init__(self, name: str, ingredients: list[str]):
        self.name = name
        self.ingredients = ingredients

    def can_make(self, pantry_set: set[str]) -> bool:
        """Check if all ingredients are in the pantry."""
        cookable = True
        for ingredient in self.ingredients:
            if ingredient not in pantry_set:
                cookable = False
        return cookable

    def missing_ingredients(self, pantry_set: set[str]) -> list[str]:
        """Return sorted list of missing ingredients."""
        return sorted(list(set(self.ingredients) - set(pantry_set)))


class Pantry:
    """Represents a pantry with a set of ingredients."""

    def __init__(self, items: list[str]):
        self.items = set(items)

    def add_ingredients(self, extra_ingredients: list[str]) -> None:
        """Add new ingredients to the pantry."""
        self.items.update(extra_ingredients)

    def has(self, ingredient: str) -> bool:
        """Check if the pantry contains an ingredient."""
        if ingredient in self.items:
            return True
        else:
            return False

    def get_items(self) -> set[str]:
        """Return the set of all items in the pantry."""
        return self.items


def create_recipes(recipe_data: dict[str, list[str]]) -> list[Recipe]:
    """Convert recipe dictionary to list of Recipe objects."""
    recipe_list = []
    
    
    for key, value in recipe_data.items():
        recipe_obj = Recipe(key, value)
        recipe_list.append(recipe_obj)

    return recipe_list


def check_recipes(recipes: list[Recipe], pantry: Pantry) -> None:
    """Check which recipes can be made and print results."""
    unique_ingredients = set()
    
    print("=== RECIPE CHECKER ===")
    
    for recipe in recipes:
        
        unique_ingredients.update(recipe.ingredients)
        
        if recipe.can_make(pantry.items):
            print(f"{recipe.name:15}: CAN MAKE ✓")
        else:
            missing_list = recipe.missing_ingredients(pantry.items)
            print(f"{recipe.name:15}: MISSING — {missing_list}")
    
    print(f"All unique ingredients ({len(unique_ingredients)}): {sorted(unique_ingredients)}")


# # Self-testing and Challenge Area #2; some of this conflicts with the code testing section based on the challenge wording of "print which recipes became newly available"
# # But if you run this instead of the challenge section, it also works
# if __name__ == "__main__":
#     # Given recipes and pantry
#     recipe_data = {
#         "omelette":        ["eggs", "butter", "salt", "pepper", "cheese"],
#         "pancakes":        ["flour", "eggs", "milk", "butter", "sugar", "salt"],
#         "tomato pasta":    ["pasta", "tomatoes", "garlic", "olive oil", "salt", "pepper"],
#         "grilled cheese":  ["bread", "cheese", "butter"],
#     }

#     pantry_items = ["eggs", "butter", "salt", "pepper", "cheese", "milk", "bread", "garlic"]

#     # Use the functions and create Pantry object
#     recipes = create_recipes(recipe_data)
#     pantry = Pantry(pantry_items)
    
#     # Initial check_recipes call
#     check_recipes(recipes, pantry)

#     # Create a start point for comparison in the challenge
#     initial_pantry_set = pantry.items

#     # List of what can be made at first
#     initial_options = []
#     for recipe in recipes:
#         if recipe.can_make(pantry.items):
#             initial_options.append(recipe.name)

#     # Ask user for more ingredients
#     new_ingredients = []
#     user_input = input("\nExtra ingredients you have (comma-separated): ")
#     for element in user_input.split(","):
#         new_ingredients.append(element.strip())
#     pantry.add_ingredients(new_ingredients)

#     # List of what can now be made
#     final_options = []
#     for recipe in recipes:
#         if recipe.can_make(pantry.items):
#             final_options.append(recipe.name)

#     # Difference between lists (sets)
#     newly_available = sorted(list(set(final_options) - set(initial_options)))

#     print()
#     check_recipes(recipes, pantry)
#     print(f"The newly available recipes are: {newly_available}")



# problem 3
from collections import Counter

class LyricAnalyzer:
    """Analyzes song lyrics for word frequency."""

    def __init__(self, lyrics: str):
        self.lyrics = lyrics
        self.words = lyrics.lower().replace(",", "").replace("!", "").replace(".", "").replace("'", "").replace("-", "").split()

    def count_words(self) -> dict[str, int]:
        """Return dictionary mapping words to their counts."""
        return dict(Counter(self.words))

    def unique_word_count(self) -> int:
        """Return the number of unique words."""
        return len(set(self.words))

    def most_common_word(self) -> tuple[str, int]:
        """Return (word, count) for the most frequent word."""
        counted_words = self.count_words()
        max_key, max_value = max(counted_words.items(), key=lambda item: item[1]) # I had to look this one up
        return max_key, max_value 

    def print_report(self) -> None:
        """Print complete word analysis report."""
        common_word, common_count = self.most_common_word()
        print("=== WORD COUNT ===")
        for key, value in dict(sorted(self.count_words().items())).items():
            print(f"{key:11}: {value}")
        
        print(f"""
Unique words: {self.unique_word_count()}
Most common word: '{common_word}' — {common_count} times
""")

    def filter_stopwords(self, stop_words: set[str]) -> None:
        """Remove stop words from the word list."""
        go_words = []
        for word in self.words:
            if word not in stop_words:
                go_words.append(word)
        self.words = go_words


# # My original self-testing section for problem 3:
# if __name__ == "__main__":
#     lyrics = """
# we will we will rock you
# we will we will rock you
# buddy youre a boy make a big noise
# playing in the street gonna be a big man someday
# you got mud on your face you big disgrace
# kicking your can all over the place singing
# we will we will rock you
# """

#     song1 = LyricAnalyzer(lyrics)
    
#     print(song1.words)
#     print(song1.count_words())
#     print(song1.most_common_word())
    
#     song1.print_report()
    
#     stop_words = {"a", "the", "you", "your", "in", "on", "we", "be", "got"}

#     song1.filter_stopwords(stop_words)

#     print('=== WITH STOPWORDS FILTERED ===')        
#     song1.print_report()



# problem 4
class Animal:
    """Represents a zoo animal with species, age, and origin."""

    def __init__(self, name: str, species: str, age: int, origin: str):
        self.name = name
        self.species = species
        self.age = age
        self.origin = origin

    def __str__(self) -> str:
        return f"{self.name.title()} ({self.species.lower()}, {self.age} years, from {self.origin.title()})"

    def get_info(self) -> None:
        """Print detailed information about the animal."""
        print(f"Name:    {self.name}")
        print(f"Species: {self.species}")
        print(f"Age:     {self.age}")
        print(f"Origin:  {self.origin}")
        

def build_registry(raw_data: list[str]) -> dict[str, Animal]:
    """Parse raw data strings and return dictionary of Animal objects."""
    
    animal_dictionary = {}
    
    for string in raw_data:
        animal_components = []
        
        clean_string = string.replace(" ", "")
        
        for component in clean_string.split(","):
            animal_components.append(component)
        
        name = animal_components[0].title()
        species = animal_components[1].lower()
        age = int(animal_components[2])
        origin = animal_components[3].title()
        
        animal_obj = Animal(name, species, age, origin)
        
        animal_dictionary[animal_obj.name] = animal_obj
        
    return animal_dictionary


def analyze_registry(registry: dict[str, Animal]) -> None:
    """Analyze and print statistics about the zoo registry."""
    species_list = []
    origins_list = []
    
    for animal in registry.values():
        species_list.append(animal.species)
        origins_list.append(animal.origin)
    
    print(f""""
=== ZOO REGISTRY BUILT ===
{len(registry)} animals registered

Unique species: {set(species_list)}
Animals come from {len(set(origins_list))} distinct regions.
""")


def group_by_species(registry: dict[str, Animal]) -> dict[str, list[Animal]]:
    """Group animals by species and return the groupings."""
    
    species_dict = {}

    for animal in registry.values():
        if animal.species in species_dict:
            pass
        else:
            species_dict[animal.species] = []
        species_dict[animal.species].append(animal)

    return species_dict


# # My original self-testing section for problem 4:
# if __name__ == "__main__":
    
#     # Provided raw data
#     raw_data = [
#         "Simba, lion, 7, Africa",
#         "Pebbles, penguin, 3, Antarctica",
#         "Kovu, lion, 4, Africa",
#         "Bubbles, dolphin, 12, Ocean",
#         "Mango, parrot, 6, South America",
#         "Nala, lion, 5, Africa",
#         "Splash, dolphin, 8, Ocean",
#         "Crackers, parrot, 2, South America",
#     ]

#     # Create the animal dictionary (build the registry) and analyze it, which includes printing results
#     animal_dictionary = build_registry(raw_data)
#     analyze_registry(animal_dictionary)
    
#     user_animal = input('Enter an animal name to look up: ').strip().title()
    
#     if user_animal not in animal_dictionary:
#         print('not found')
#     else:
#         print()
#         animal_dictionary[user_animal].get_info()
    
#     # Challenge section
#     print("=== ANIMALS BY SPECIES ===")               # I got this title card by looking at the code testing section
#     species_dict = group_by_species(animal_dictionary)
#     for species, animals in species_dict.items():
        
#         animal_names = []
        
#         for animal in animals:
#             animal_names.append(animal.name)
            
#         print(f"{species:8}: {', '.join(animal_names)}")




# I kept testing code exactly the same from the solutions file so as to preserve validation
if __name__ == "__main__":
    TESTING_PROBLEM = 3

    if TESTING_PROBLEM == 1:
        reports = [
            "SANTOS | Private | Fitness:91 | Status:available",
            "KOWALSKI | Corporal | Fitness:74 | Status:deployed",
            "OKAFOR | Sergeant | Fitness:88 | Status:available",
            "BRIGGS | Private | Fitness:55 | Status:available",
            "NAKAMURA | Corporal | Fitness:82 | Status:deployed",
            "REYES | Sergeant | Fitness:79 | Status:available",
        ]

        roster, ranks = process_reports(reports)

        print("=== ROSTER LOADED ===")
        print(f"{len(roster)} soldiers on record.")
        print(f"Ranks on file: {ranks}\n")

        show_available(roster)

        dispatch(roster, "Santos")
        dispatch(roster, "Kowalski")
        print("\nUpdated status:")
        for name in ["Santos", "Kowalski"]:
            soldier = roster.get(name.title())
            status = "deployed" if soldier.deployed else "available"
            print(f"  {name:8}: {status}")

        print("\nFitness report:")
        report = fitness_report(roster)
        for band in ("high", "medium", "low"):
            print(f"  {band.title():6}: {report[band]}")

    elif TESTING_PROBLEM == 2:
        recipe_data = {
            "omelette": ["eggs", "butter", "salt", "pepper", "cheese"],
            "pancakes": ["flour", "eggs", "milk", "butter", "sugar", "salt"],
            "tomato pasta": [
                "pasta",
                "tomatoes",
                "garlic",
                "olive oil",
                "salt",
                "pepper",
            ],
            "grilled cheese": ["bread", "cheese", "butter"],
        }
        pantry_items = [
            "eggs",
            "butter",
            "salt",
            "pepper",
            "cheese",
            "milk",
            "bread",
            "garlic",
        ]

        recipes = create_recipes(recipe_data)
        pantry = Pantry(pantry_items)

        check_recipes(recipes, pantry)

        raw = input("\nExtra ingredients you have (comma-separated): ")
        extras = []
        for item in raw.split(","):
            extras.append(item.strip())
        pantry.add_ingredients(extras)

        print()
        check_recipes(recipes, pantry)

    elif TESTING_PROBLEM == 3:
        lyrics = """
we will we will rock you
we will we will rock you
buddy youre a boy make a big noise
playing in the street gonna be a big man someday
you got mud on your face you big disgrace
kicking your can all over the place singing
we will we will rock you
"""

        analyzer = LyricAnalyzer(lyrics)
        analyzer.print_report()

        print("\n=== WITH STOPWORDS FILTERED ===")
        stop_words = {"a", "the", "you", "your", "in", "on", "we", "be", "got"}
        analyzer.filter_stopwords(stop_words)
        analyzer.print_report()

    elif TESTING_PROBLEM == 4:
        raw_data = [
            "Simba, lion, 7, Africa",
            "Pebbles, penguin, 3, Antarctica",
            "Kovu, lion, 4, Africa",
            "Bubbles, dolphin, 12, Ocean",
            "Mango, parrot, 6, South America",
            "Nala, lion, 5, Africa",
            "Splash, dolphin, 8, Ocean",
            "Crackers, parrot, 2, South America",
        ]

        registry = build_registry(raw_data)
        analyze_registry(registry)

        name_input = input("Enter an animal name to look up: ")
        name = name_input.strip().title()

        if name in registry:
            print()
            registry[name].get_info()
        else:
            print(f"\n{name} not found in registry.")

        print("\n=== ANIMALS BY SPECIES ===")
        by_species = group_by_species(registry)
        for species, animals in by_species.items():
            names = []
            for animal in animals:
                names.append(animal.name)
            print(f"{species:8}: {', '.join(names)}")

    else:
        print("There are only 4 problems!")
