

#**Create a `Soldier` class** 
class Soldier:
    def __init__(self, name, rank, fitness, deployed):
        self.name = name
        self.rank = rank
        self.fitness = fitness
        self.deployed = deployed

    def dispatch(self):
        self.deployed = True

    def __str__(self):
        return f"{self.name} ({self.rank}, fitness: {self.fitness}, deployed: {self.deployed})"


def process_reports(reports):
    roster = {}
    ranks = set()

    for report in reports:
        parts = report.split("|")

        name = parts[0].strip()
        rank = parts[1].strip()
        fitness = parts[2].strip()
        status = parts[3].strip()

        fitness = fitness.split(":")[1]
        status = status.split(":")[1]

        name = name.title()
        rank = rank.upper()
        status = status.lower()
        fitness = int(fitness)

        deployed = status == "deployed"

        soldier = Soldier(name, rank, fitness, deployed)

        roster[name] = soldier
        ranks.add(rank)

    return roster, ranks


def show_available(roster):
    available_names = []

    for name in roster:
        soldier = roster[name]

        if soldier.deployed == False:
            available_names.append(name)

    available_names.sort()

    for name in available_names:
        print(name)


def dispatch(roster, name):
    name = name.title()

    if name not in roster:
        print(f"{name} not found")
        return

    soldier = roster[name]

    if soldier.deployed:
        print(f"{name} is already deployed.")
    else:
        soldier.dispatch()
        print(f"{name} dispatched. Status set to deployed.")


def fitness_report(roster):
    report = {
        "high": [],
        "medium": [],
        "low": []
    }

    for name in roster:
        soldier = roster[name]

        if soldier.fitness >= 80:
            report["high"].append(name)

        elif soldier.fitness >= 60:
            report["medium"].append(name)

        else:
            report["low"].append(name)

    report["high"].sort()
    report["medium"].sort()
    report["low"].sort()

    return report


# ONLY RUNS WHEN YOU EXECUTE THIS FILE DIRECTLY
if __name__ == "__main__":

    reports = [
        "SANTOS | Private | Fitness:91 | Status:available",
        "KOWALSKI | Corporal | Fitness:74 | Status:deployed",
        "OKAFOR | Sergeant | Fitness:88 | Status:available",
        "BRIGGS | Private | Fitness:55 | Status:available",
        "NAKAMURA | Corporal | Fitness:82 | Status:deployed",
        "REYES | Sergeant | Fitness:79 | Status:available"
    ]

    roster, ranks = process_reports(reports)

    print("=== ROSTER LOADED ===")
    print(f"{len(roster)} soldiers on record.")
    print(f"Ranks on file: {ranks}")

    print("\nAvailable soldiers:")
    show_available(roster)

    print("\nDispatching Santos...")
    dispatch(roster, "Santos")

    print("\nDispatching Kowalski...")
    dispatch(roster, "Kowalski")

    print("\nUpdated Status:")
    print(f"Santos: {'deployed' if roster['Santos'].deployed else 'available'}")
    print(f"Kowalski: {'deployed' if roster['Kowalski'].deployed else 'available'}")

    print("\nFitness Report:")
    print(fitness_report(roster))




################

recipe_data = {
    "omelette":        ["eggs", "butter", "salt", "pepper", "cheese"],
    "pancakes":        ["flour", "eggs", "milk", "butter", "sugar", "salt"],
    "tomato pasta":    ["pasta", "tomatoes", "garlic", "olive oil", "salt", "pepper"],
    "grilled cheese":  ["bread", "cheese", "butter"],
}

pantry_items = [
    "eggs",
    "butter",
    "salt",
    "pepper",
    "cheese",
    "milk",
    "bread",
    "garlic"
]


class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def can_make(self, pantry_items):
        for ingredient in self.ingredients:
            if ingredient not in pantry_items:
                return False
        return True

    def missing_ingredients(self, pantry_set):
        missing = []

        for ingredient in self.ingredients:
            if ingredient not in pantry_set:
                missing.append(ingredient)

        missing.sort()

        return missing


class Pantry:
    def __init__(self, pantry_items):
        self.ingredients = set(pantry_items)

    def add_ingredients(self, extra_ingredients):
        self.ingredients.update(extra_ingredients)

    def has(self, ingredient):
        return ingredient in self.ingredients

    def get_items(self):
        return self.ingredients


def create_recipes(recipe_data):
    recipes = []

    for recipe_name in recipe_data:
        ingredients = recipe_data[recipe_name]

        new_recipe = Recipe(recipe_name, ingredients)

        recipes.append(new_recipe)

    return recipes


def check_recipes(recipes, pantry):
    all_ingredients = set()

    for recipe in recipes:

        if recipe.can_make(pantry.get_items()):
            print(f"{recipe.name:<15}: CAN MAKE ✓")
        else:
            print(
                f"{recipe.name:<15}: MISSING — {recipe.missing_ingredients(pantry.get_items())}"
            )

        all_ingredients.update(recipe.ingredients)

    sorted_ingredients = sorted(all_ingredients)

    print(
        f"\nAll unique ingredients ({len(sorted_ingredients)}): {sorted_ingredients}"
    )



if __name__ == "__main__":

    print("=== RECIPE CHECKER ===")

    pantry = Pantry(pantry_items)
    recipes = create_recipes(recipe_data)

    # First check
    check_recipes(recipes, pantry)


    # Challenge section
    print("\nAdd extra ingredients to your pantry:")

    user_input = input("> ")

    extra_ingredients = [
        ingredient.strip()
        for ingredient in user_input.split(",")
    ]

    pantry.add_ingredients(extra_ingredients)



    print("\n=== UPDATED RECIPE CHECK ===")

    check_recipes(recipes, pantry)





################################################################

class LyricAnalyzer:
    def __init__(self, lyrics):
        self.lyrics = lyrics

        processed = lyrics.lower()
        processed = processed.replace(".", "")
        processed = processed.replace(",", "")
        processed = processed.replace("!", "")
        processed = processed.replace(":", "")
        processed = processed.replace("'", "")
        processed = processed.replace('"', "")
        processed = processed.replace("?", "")

        self.words = processed.split()


    def count_words(self):
        counts = {}

        for word in self.words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

        return counts


    def unique_word_count(self):
        return len(set(self.words))


    def most_common_word(self):
        counts = self.count_words()

        word = max(counts, key=counts.get)

        return (word, counts[word])


    # ADD THIS METHOD
    def filter_stopwords(self, stop_words):
        filtered_words = []

        for word in self.words:
            if word not in stop_words:
                filtered_words.append(word)

        self.words = filtered_words


    def print_report(self):
        counts = self.count_words()

        print("=== WORD COUNT ===")

        for word in sorted(counts):
            print(f"{word}: {counts[word]}")

        print(f"Unique words: {self.unique_word_count()}")

        word, count = self.most_common_word()

        print(f"Most common word: {word} -- {count} times")


###################################################################################

class Animal:
    def __init__(self, name, species, age, origin):
        self.name = name
        self.species = species
        self.age = age
        self.origin = origin

    def __str__(self):
        return f"{self.name} ({self.species}, {self.age} years, from {self.origin})"

    def get_info(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Age: {self.age} years")
        print(f"Origin: {self.origin}")


def build_registry(raw_data):
    registry = {}

    for entry in raw_data:
        parts = entry.split(",")

        name = parts[0].strip()
        species = parts[1].strip()
        age = parts[2].strip()
        origin = parts[3].strip()

        age = int(age)

        animal = Animal(name, species, age, origin)

        registry[name] = animal

    return registry


def analyze_registry(registry):
    species = set()
    origins = set()

    for name in registry:
        animal = registry[name]

        species.add(animal.species)
        origins.add(animal.origin)

    print(f"Total animals: {len(registry)}")
    print(f"Unique species: {species}")
    print(f"Distinct origins: {len(origins)}")

def group_by_species(registry):
    grouped = {}

    for name in registry:
        animal = registry[name]

        species = animal.species

        if species not in grouped:
            grouped[species] = []

        grouped[species].append(animal)
    return grouped

   




if __name__ == "__main__":

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

    grouped = group_by_species(registry)

    for species, animals in grouped.items():
        name = []

        for animal in animals:
            name.append(animal.name)

        print(f"{species}: {', '.join(name)}")


    animal_name = input("\nEnter animal name: ")

    animal_name = animal_name.strip().title()

    if animal_name in registry:
        registry[animal_name].get_info()
    else:
        print("Animal not found")


        

