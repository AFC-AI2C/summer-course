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
    for report in reports:    
        report_as_list = report.split("|")
        report_as_list = [an_item.strip() for an_item in report_as_list]
        sldr_keys = ["name", "rank", "fitness", "deployed"]
        report_as_dict = dict(zip(sldr_keys, report_as_list))
        # Processes name.
        report_as_dict["name"] = report_as_dict["name"].title()
        # Pocesses rank.
        report_as_dict["rank"] = report_as_dict["rank"].upper()
        # Processes fitness.
        report_as_dict["fitness"] = int(report_as_list[2].split(":")[1])
        # Processes deployed.
        report_as_dict["deployed"] = report_as_list[3].split(":")[1]
        if report_as_dict["deployed"] == "available":
            report_as_dict["deployed"] = False
        elif report_as_dict["deployed"] == "deployed":
            report_as_dict["deployed"] = True
#        report_as_dict["deployed"].lower()  # Per assignment specifications.
        report_as_list = [report_as_dict["name"], report_as_dict["rank"], report_as_dict["fitness"], report_as_dict["deployed"]]
        roster[report_as_dict["name"]] = Soldier(*report_as_list)
        unique_ranks.add(report_as_dict["rank"])
    return (roster, unique_ranks)


def show_available(roster: dict[str, Soldier]) -> None:
    """Display all available soldiers, sorted alphabetically."""
    available_soldiers = {k:v for k,v in roster.items() if v.deployed == False}
    alphabetic_available = list(available_soldiers.keys())
    alphabetic_available.sort()
#    for s_name in alphabetic_available:
#        print(available_soldiers[s_name])
    print(alphabetic_available)

def dispatch(roster: dict[str, Soldier], name: str) -> None:
    """Dispatch a soldier by name, or print an error if not available."""
    if name in roster:
        if roster[name].deployed == True:
            print(f"Dispatching {name}...\t\t{name} is already deployed.")
        else:
            roster[name].dispatch()
            print(f"Dispatching {name}...\t\tDone. Status set to deployed.")


def fitness_report(roster: dict[str, Soldier]) -> dict[str, list[str]]:
    """Return a dict with 'high', 'medium', 'low' fitness bands."""
    high_list = []
    med_list = []
    low_list = []
    for name in roster:
        if roster[name].fitness >= 80:
            high_list.append(name)
        elif roster[name].fitness >= 60:
            med_list.append(name)
        else:
            low_list.append(name)
    high_list.sort()
    med_list.sort()
    low_list.sort()
    return {"high": high_list, "medium": med_list, "low": low_list}

if __name__ == "__main__":
    reports = [
        "SANTOS | Private | Fitness:91 | Status:available",
        "KOWALSKI | Corporal | Fitness:74 | Status:deployed",
        "OKAFOR | Sergeant | Fitness:88 | Status:available",
        "BRIGGS | Private | Fitness:55 | Status:available",
        "NAKAMURA | Corporal | Fitness:82 | Status:deployed",
        "REYES | Sergeant | Fitness:79 | Status:available",
    ]
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

# problem 2
class Recipe:
    """Represents a recipe with a name and list of ingredients."""

    def __init__(self, name: str, ingredients: list[str]):
        pass

    def can_make(self, pantry_set: set[str]) -> bool:
        """Check if all ingredients are in the pantry."""
        pass

    def missing_ingredients(self, pantry_set: set[str]) -> list[str]:
        """Return sorted list of missing ingredients."""
        pass


class Pantry:
    """Represents a pantry with a set of ingredients."""

    def __init__(self, items: list[str]):
        pass

    def add_ingredients(self, extra_ingredients: list[str]) -> None:
        """Add new ingredients to the pantry."""
        pass

    def has(self, ingredient: str) -> bool:
        """Check if the pantry contains an ingredient."""
        pass

    def get_items(self) -> set[str]:
        """Return the set of all items in the pantry."""
        pass


def create_recipes(recipe_data: dict[str, list[str]]) -> list[Recipe]:
    """Convert recipe dictionary to list of Recipe objects."""
    pass


def check_recipes(recipes: list[Recipe], pantry: Pantry) -> None:
    """Check which recipes can be made and print results."""
    pass


# problem 3
class LyricAnalyzer:
    """Analyzes song lyrics for word frequency."""

    def __init__(self, lyrics: str):
        pass

    def count_words(self) -> dict[str, int]:
        """Return dictionary mapping words to their counts."""
        pass

    def unique_word_count(self) -> int:
        """Return the number of unique words."""
        pass

    def most_common_word(self) -> tuple[str, int]:
        """Return (word, count) for the most frequent word."""
        pass

    def print_report(self) -> None:
        """Print complete word analysis report."""
        pass

    def filter_stopwords(self, stop_words: set[str]) -> None:
        """Remove stop words from the word list."""
        pass


# problem 4
class Animal:
    """Represents a zoo animal with species, age, and origin."""

    def __init__(self, name: str, species: str, age: int, origin: str):
        pass

    def __str__(self) -> str:
        pass

    def get_info(self) -> None:
        """Print detailed information about the animal."""
        pass


def build_registry(raw_data: list[str]) -> dict[str, Animal]:
    """Parse raw data strings and return dictionary of Animal objects."""
    pass


def analyze_registry(registry: dict[str, Animal]) -> None:
    """Analyze and print statistics about the zoo registry."""
    pass


def group_by_species(registry: dict[str, Animal]) -> dict[str, list[Animal]]:
    """Group animals by species and return the groupings."""
    pass

# This will only execute if this script is executed directly, not imported
if __name__ == "__main__":
    # you can use this variable to test problems independently
    # while you're working locally
    TESTING_PROBLEM = 1

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

    else:
        print("There are only 4 problems!")
