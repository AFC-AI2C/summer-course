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
        return f"{self.name} ({self.rank}, fitness: {self.fitness}, deployed: {self.deployed})"


def process_reports(report_list: list[str]) -> tuple[dict[str, Soldier], set[str]]:
    """Parse report strings and return (roster_dict, ranks_set)."""
    roster = dict()
    unique_ranks = set()
    for report in report_list:    
        raw_name, raw_rank, raw_fitness, raw_status = report.split("|")
        name = raw_name.strip().title()
        rank = raw_rank.strip().upper()
        fitness_val = int(raw_fitness.split(":")[1].strip())
        status_val = raw_status.split(":")[1].strip().lower()
        deployed = status_val == "deployed"
        soldier = Soldier(name, rank, fitness_val, deployed)
        roster[name] = soldier
        unique_ranks.add(rank)
    return roster, unique_ranks


def show_available(roster: dict[str, Soldier]) -> None:
    """Display all available soldiers, sorted alphabetically."""
    available_names = [s.name for s in roster.values() if not s.deployed]
    available_names.sort()
    print(available_names)

def dispatch(roster: dict[str, Soldier], name: str) -> None:
    """Dispatch a soldier by name, or print an error if not available."""
    name = name.title()
    if name in roster.keys():
        if roster[name].deployed:
            print(f"Dispatching {name}...\t\t{name} is already deployed.")
        else:
            roster[name].dispatch()
            print(f"Dispatching {name}...\t\tDone. Status set to deployed.")
    else:
        print(f"Soldier '{name}' not found in roster.")

def fitness_report(roster: dict[str, Soldier]) -> dict[str, list[str]]:
    """Return a dict with 'high', 'medium', 'low' fitness bands."""
    report = {"high": [], "medium": [], "low": []}
    for soldier in roster.values():
        if soldier.fitness >= 80:
            report["high"].append(soldier.name)
        elif soldier.fitness >= 60:
            report["medium"].append(soldier.name)
        else:
            report["low"].append(soldier.name)
    for group in report:
        report[group].sort()
    return report


# problem 2
class Recipe:
    """Represents a recipe with a name and list of ingredients."""

    def __init__(self, name: str, ingredients: list[str]):
        self.name = name
        self.ingredients = ingredients

    def can_make(self, pantry_set: set[str]) -> bool:
        """Check if all ingredients are in the pantry."""
#        return all(ingredient in pantry_set for ingredient in self.ingredients) # Equivalent result to line below.
        return set(self.ingredients).issubset(pantry_set)
#       return set(self.ingredients) <= pantry_set # Equivalent result to line above.

    def missing_ingredients(self, pantry_set: set[str]) -> list[str]:
        """Return sorted list of missing ingredients."""
        unavailable_items = []
        for ingredient in self.ingredients:
            if ingredient not in pantry_set:
                unavailable_items.append(ingredient)
        unavailable_items.sort()
        return unavailable_items


class Pantry:
    """Represents a pantry with a set of ingredients."""

    def __init__(self, items: list[str]):
        self.items = set(items)

    def add_ingredients(self, extra_ingredients: list[str]) -> None:
        """Add new ingredients to the pantry."""
        self.items.update(extra_ingredients)

    def has(self, ingredient: str) -> bool:
        """Check if the pantry contains an ingredient."""
        return ingredient in self.items

    def get_items(self) -> set[str]:
        """Return the set of all items in the pantry."""
        return self.items


def create_recipes(recipe_data: dict[str, list[str]]) -> list[Recipe]:
    """Convert recipe dictionary to list of Recipe objects."""
    #return [Recipe(*item) for item in recipe_data.items()] # Equivalent to next line.
    return [Recipe(name, ingredients) 
        for name, ingredients in recipe_data.items()
    ]


def check_recipes(recipes: list[Recipe], pantry: Pantry) -> None:
    """Check which recipes can be made and print results."""
    for recipe in recipes:
        if all(pantry.has(ingredient) for ingredient in recipe.ingredients):
            print(f"{recipe.name:15}: CAN MAKE")
        else:
            print(f"{recipe.name:15}: MISSING - {recipe.missing_ingredients(pantry.get_items())}")
    all_ingredients = list({ingredient for recipe in recipes for ingredient in recipe.ingredients})
    all_ingredients.sort()
    print(f"All unique ingredients ({len(all_ingredients)}): {all_ingredients}")


# Did not attempt challenge.


# problem 3
class LyricAnalyzer:
    """Analyzes song lyrics for word frequency."""

    def __init__(self, lyrics: str):
        self.lyrics = lyrics
        # can do the following instead
        #punctuation = ":,.!\"';"
        #for punct in punctuation:
        #   lyrics.replace(punct, "")
        self.words = lyrics.lower().replace(',', '').replace('.', '').replace('!', '').replace("'", "").replace('"', '').replace('?', '').replace(';', '').split()

    def count_words(self) -> dict[str, int]:
        """Return dictionary mapping words to their counts."""
        word_set = set(self.words)
        return {word:sum([lyric == word for lyric in self.words]) for word in word_set} 

    def unique_word_count(self) -> int:
        """Return the number of unique words."""
        return len(set(self.words))

    def most_common_word(self) -> tuple[str, int]:
        """Return (word, count) for the most frequent word."""
        word_counts = self.count_words()
        words_by_freq = sorted(word_counts, key=lambda word: word_counts[word])
        word, count = words_by_freq[-1], word_counts[words_by_freq[-1]]
#        word = [word for word, freq in word_counts.items() if freq == count]
#        if len(word) == 1:
#            word = word[0]
        return (word, count)

    def print_report(self) -> None:
        """Print complete word analysis report."""
        # Prints word counts in alphabetical order.
        alphabetical_list = sorted(set(self.words))
        max_word_length = max([len(word) for word in alphabetical_list])
        word_counts = self.count_words()
        for word in alphabetical_list:
            print(f"{word:<{max_word_length}}: {word_counts[word]}")
        print('')
        print(f'Unique words: {self.unique_word_count()}')
        word, count = self.most_common_word()
        print(f"Most common word: '{word}' - {count} times")
        print('')

    def filter_stopwords(self, stop_words: set[str]) -> None:
        """Remove stop words from the word list.""" 
        self.words = [word for word in self.words if word not in stop_words]
        self.print_report()


# problem 4
class Animal:
    """Represents a zoo animal with species, age, and origin."""

    def __init__(self, name: str, species: str, age: int, origin: str):
        self.name = name
        self.species = species
        self.age = age
        self.origin = origin

    def __str__(self) -> str:
        return f"{self.name} ({self.species}, {self.age} years, from {self.origin})"

    def get_info(self) -> None:
        """Print detailed information about the animal."""
        print(f"Name:\t {self.name}\nSpecies: {self.species}\nAge:\t {self.age}\nOrigin:\t {self.origin}\n")


def build_registry(raw_data: list[str]) -> dict[str, Animal]:
    """Parse raw data strings and return dictionary of Animal objects."""
    registry = {}
    for entry in raw_data:
        name, species, age, origin = [field.strip() for field in entry.split(',')]
        registry[name] = Animal(name, species, int(age), origin)
    return registry


def analyze_registry(registry: dict[str, Animal]) -> None:
    """Analyze and print statistics about the zoo registry."""
    print(f"{len(registry)} animals registered.")
    unique_species = {animal.species for animal in registry.values()}
    print(f"Unique species: {unique_species}")
    origins = {animal.origin for animal in registry.values()}
    print(f"Animals come from {len(origins)} distinct regions.")
    print()

def group_by_species(registry: dict[str, Animal]) -> dict[str, list[Animal]]:
    """Group animals by species and return the groupings."""
    pass


# This will only execute if this script is executed directly, not imported
if __name__ == "__main__":
    # you can use this variable to test problems independently
    # while you're working locally
    TESTING_PROBLEM = 4

    if TESTING_PROBLEM == 1:
        reports = [
            "SANTOS | Private | Fitness:91 | Status:available",
            "KOWALSKI | Corporal | Fitness:74 | Status:deployed",
            "OKAFOR | Sergeant | Fitness:88 | Status:available",
            "BRIGGS | Private | Fitness:55 | Status:available",
            "NAKAMURA | Corporal | Fitness:82 | Status:deployed",
            "REYES | Sergeant | Fitness:79 | Status:available",
        ]

        # add your own testing here for problem 1
        my_roster, my_unique_ranks = process_reports(reports)
        print(my_unique_ranks)
        show_available(my_roster)
        my_checks = ["Santos", "Kowalski"]
        for s_name in my_checks:
            dispatch(my_roster, s_name)
        for s_name in my_checks:
            if my_roster[s_name.title()].deployed == True:
                print(f"{s_name:<15}: deployed")
            else:
                print(f"{s_name:<15}: available")
        print(fitness_report(roster=my_roster))

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

        # add your own testing here for problem 2
        recipes = create_recipes(recipe_data)
        pantry = Pantry(pantry_items)
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
        # add your own testing here for problem 3
        lyrics = """
            High school seemed like such a blur
            I didn't have much interest in sports or school elections
            And in class I dreamed all day
            Of a rock 'n' roll weekend

            And the girl in the front of the room
            So close yet so far, y'know she never seemed to notice
            That this silly schoolboy crush
            Wasn't just pretend

            Life goes by so fast
            You only want to do what you think is right
            Close your eyes and then it's past;
            Story of my life

            And I went down my old neighborhood
            The faces have all changed, there's no one left to talk to
            And the pool hall I loved as a kid
            Is now a 7-11

            I went downtown to look for a job
            I had no training, no experience to speak of
            I looked at the holes in my jeans
            And turned and headed back
            See Social Distortion Live
            Get tickets as low as $83

            Life goes by so fast
            You only want to do what you think is right
            Close your eyes and then it's past;
            Story of my life

            And good times come and good times go
            I only wish the good times would last a little longer
            And I think about the good times we had
            And why they had to end

            So I sit at the edge of my bed
            I strum my guitar and I sing an outlaw love song
            Thinkin' about what you're doin' now
            And when you're coming back

            Life goes by so fast
            You only want to do what you think is right
            Close your eyes and then it's past;
            Story of my life
        """
        analysis = LyricAnalyzer(lyrics)
        analysis.print_report()
        stop_words = {"a", "the", "you", "your", "in", "on", "we", "be", "got", "and", "i", "of", "to", "so"}
        analysis.filter_stopwords(stop_words)

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

        # add your own testing here for problem 4
        registry = build_registry(raw_data)
        analyze_registry(registry)
        name = input("Enter an animal name to look up: ").strip().title()
        print()
        if registry.get(name):
            registry[name].get_info()
        else:
            print("not found")


    else:
        print("There are only 4 problems!")
