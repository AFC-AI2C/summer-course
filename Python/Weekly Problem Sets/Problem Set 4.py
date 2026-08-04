#if __name__ == "__main__":

# ## Problem 1 — Soldier Roster & Dispatch System 🪖

# *HQ needs a searchable roster of available soldiers. Your program will parse incoming personnel reports using custom classes to represent each soldier.*

# **You are given the following personnel reports as raw strings:**

# ```python
# reports = [
#     "SANTOS | Private | Fitness:91 | Status:available",
#     "KOWALSKI | Corporal | Fitness:74 | Status:deployed",
#     "OKAFOR | Sergeant | Fitness:88 | Status:available",
#     "BRIGGS | Private | Fitness:55 | Status:available",
#     "NAKAMURA | Corporal | Fitness:82 | Status:deployed",
#     "REYES | Sergeant | Fitness:79 | Status:available",
# ]
# ```

# **Your task:**

# - **Create a `Soldier` class** with the following:
#   -#### An `__init__` method that accepts `name`, `rank`, `fitness`, and `deployed` parameters
#   -####Store these as instance attributes using `self.name`, `self.rank`, `self.fitness`, and `self.deployed`
#   -#### Add a `dispatch()` method that sets `self.deployed = True`
#   -#### Add a `__str__` method that returns a formatted string with the soldier's information (e.g., `"Santos (PRIVATE, fitness: 91, deployed: False)"`)

# - #### Create a function named `process_reports()` that:
#   - ####Takes a list of report strings as input
#   - ####Returns two values: a dictionary of `Soldier` objects (keyed by name), and a set of unique ranks
#   - ####Use a `for` loop to parse each report string with `.split("|")`, `.strip()`, and `.split(":")`
#   - ####Use `.title()` on names, `.upper()` on ranks, and `.lower()` on status values to normalise the data
#   - ####Create a `Soldier` object for each report and add it to the roster dictionary
#   - ####Collect all unique ranks in a set

# - ####Write a function `show_available(roster)` that:
#   - ####Prints all soldiers where `deployed` is `False`, sorted alphabetically by name
#   - ####Use `.sort()` on the list of available names

# - ####Write a function `dispatch(roster, name)` that:
#   - ####Takes the roster dictionary and a soldier's name
#   - ####Calls the `.dispatch()` method on the appropriate `Soldier` object
#   - ####Prints a message if they are already deployed or not found

# **Expected output (partial):**

# ```
# === ROSTER LOADED ===
# 6 soldiers on record.
# Ranks on file: {'PRIVATE', 'CORPORAL', 'SERGEANT'}

# Available soldiers: ['Briggs', 'Okafor', 'Reyes', 'Santos']

# Dispatching Santos...   Done. Status set to deployed.
# Dispatching Kowalski... Kowalski is already deployed.

# Updated status:
#   Santos   : deployed
#   Kowalski : deployed
# ```


reports = [
    "SANTOS | Private | Fitness:91 | Status:available",
    "KOWALSKI | Corporal | Fitness:74 | Status:deployed",
    "OKAFOR | Sergeant | Fitness:88 | Status:available",
    "BRIGGS | Private | Fitness:55 | Status:available",
    "NAKAMURA | Corporal | Fitness:82 | Status:deployed",
    "REYES | Sergeant | Fitness:79 | Status:available"
    ]


#**Create a `Soldier` class** 
class Soldier:

    #An `__init__` method 

    def __init__(self, name, rank, fitness, deployed):

        #Store these as instance attributes

        self.name = name
        self.rank = rank
        self.fitness = fitness
        self.deployed = deployed

    #Add a `dispatch()` method that sets `self.deployed = True`

    def dispatch(self):
        self.deployed = True

    # Add a `__str__` method

    def __str__(self)->str:
        return(
                f"{self.name} ({self.rank.upper()}, fitness: {self.fitness}, deployed: {self.deployed})"
                )



### Create a function named `process_reports()   

def process_reports (reports):

    ranks = set()
    roster = {}

    #Use a `for` loop to parse each report string with `.split("|")`, `.strip()`, and `.split(":")`
    for report in reports:

        #break the report apart
        parts = report.split("|")
        
        #extract each pieces 
        name = parts[0].strip()
        rank = parts[1].strip()      
        fitness = parts[2].strip()
        status = parts[3].strip()

        # split the key/vaules pairs 
        fitness = fitness.split(":")[1]
        status = status.split(":")[1]

        #Use `.title()` on names, `.upper()` on ranks, and `.lower()` on status values to normalise the data
        #normalize the date
        name = name.title()
        rank =rank.upper()
        status =status.lower()
        fitness = int(fitness)

    

        #Create a `Soldier` object for each report and add it to the roster dictionary
        deployed = status =="deployed"

        soldier = Soldier(name,rank,fitness,deployed)

#Collect all unique ranks in a set
        roster[name] = soldier
        ranks.add(rank)

    return roster, ranks



#Write a function `show_available(roster)
      
def show_available(roster):

#Prints all soldiers where `deployed` is `False`, sorted alphabetically by name


    available_names =[]

    for name in roster:
        soldier = roster[name]

        if not soldier.deployed:
            available_names.append(name)

    available_names.sort()
    
    print(available_names)


    




# - Write a function `dispatch(roster, name)` that:




def dispatch(roster, name):
    name = name.title()
    if name in roster:
        soldier = roster[name]

#   - Takes the roster dictionary and a soldier's name
        if soldier.deployed:
            print(f"{name} is already deployed")


#   - Calls the `.dispatch()` method on the appropriate `Soldier` object
        else:
            soldier.dispatch()
            print("Done. Status set to deployed. ")

#   - Prints a message if they are already deployed or not found
    else:
        print(f"{name} not found")


# **Expected output (partial):**

# ```
# === ROSTER LOADED ===
# 6 soldiers on record.
# Ranks on file: {'PRIVATE', 'CORPORAL', 'SERGEANT'}

# Available soldiers: ['Briggs', 'Okafor', 'Reyes', 'Santos']

# Dispatching Santos...   Done. Status set to deployed.
# Dispatching Kowalski... Kowalski is already deployed.

# Updated status:
#   Santos   : deployed
#   Kowalski : deployed
# ```

roster, ranks = process_reports(reports)
print("=== ROSTER LOADED ===")
print(f"{len(roster)} soldiers on record.")
print(f"Ranks on file: {ranks}")

available = show_available(roster)
print(f"Available soldiers: {available}")

print("Dispatching Santos...")
dispatch(roster, "Santos")

print("Dispatching Kowalski...")
dispatch(roster, "Kowalski")

print("\nUpdated Status:")

print(f"Santos : {'deployed' if roster['Santos'].deployed else 'available'}")
print(f"Kowalski : {'deployed' if roster['Kowalski'].deployed else 'available'}")


# ### Challenge

#Write a function `fitness_report(roster)` that builds and returns a dictionary with three keys —
# `"high"`, `"medium"`, and `"low"` — each mapping to a list of soldier names in that fitness band (high ≥ 80, medium 60–79, low < 60). Access the `fitness` attribute from each `Soldier` object using a `for` loop. Use `.append()` to build each list and `.sort()` to sort the names. Print the full report.

def fitness_report(roster):

    report = {
        "high" :[],
        "medium" : [],
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

fitness = fitness_report(roster)
print("\n Fitness Report:")
for level, soldier in fitness.items():
    print(f"{level}: {soldier}")


############################################################################################################################################
# ## Problem 2 — Recipe Ingredient Checker 🍳

# *You're building a tool that helps cooks figure out what they can make with what's in their kitchen, and what they're missing.*

# **You are given the following recipes and pantry:**

# ```python
# recipe_data = {
#     "omelette":        ["eggs", "butter", "salt", "pepper", "cheese"],
#     "pancakes":        ["flour", "eggs", "milk", "butter", "sugar", "salt"],
#     "tomato pasta":    ["pasta", "tomatoes", "garlic", "olive oil", "salt", "pepper"],
#     "grilled cheese":  ["bread", "cheese", "butter"],
# }

# pantry_items = ["eggs", "butter", "salt", "pepper", "cheese", "milk", "bread", "garlic"]
# ```

# **Your task:**

# - **Create a `Recipe` class** with the following:
#   - An `__init__` method that accepts `name` and `ingredients` (a list of strings)
#   - Store these as instance attributes
#   - Add a `can_make(pantry_set)` method that returns `True` if all ingredients are in the pantry set, `False` otherwise
#   - Add a `missing_ingredients(pantry_set)` method that returns a **sorted list** of ingredients not in the pantry

# - **Create a `Pantry` class** with the following:
#   - An `__init__` method that accepts a list of ingredient strings
#   - Store the ingredients internally as a **set** for efficient lookups
#   - Add an `add_ingredients(extra_ingredients)` method that adds new ingredients to the pantry
#   - Add a `has(ingredient)` method that returns `True` if the ingredient is in the pantry

# - Create a function `create_recipes(recipe_data)` that:
#   - Takes the recipe dictionary shown above
#   - Returns a list of `Recipe` objects

# - Create a function `check_recipes(recipes, pantry)` that:
#   - Takes a list of `Recipe` objects and a `Pantry` object
#   - Uses a `for` loop to check each recipe
#   - Prints whether each recipe can be made and — if not — what's missing
#   - At the end, print a list of all **unique ingredients** across all recipes, sorted alphabetically

# **Expected output:**

# ```
# === RECIPE CHECKER ===
# omelette       : CAN MAKE ✓
# pancakes       : MISSING — ['flour', 'sugar']
# tomato pasta   : MISSING — ['olive oil', 'pasta', 'tomatoes']
# grilled cheese : CAN MAKE ✓

# All unique ingredients (13): ['bread', 'butter', 'cheese', 'eggs', ...]
# ```

# ### Challenge

# In your `__main__` block, ask the user for a comma-separated list of extra ingredients, parse them with `.split(",")` and `.strip()`, 
# add them to the pantry using the `.add_ingredients()` method, then call `check_recipes()` 
# again and print which recipes became newly available.



recipe_data = {
    "omelette":        ["eggs", "butter", "salt", "pepper", "cheese"],
    "pancakes":        ["flour", "eggs", "milk", "butter", "sugar", "salt"],
    "tomato pasta":    ["pasta", "tomatoes", "garlic", "olive oil", "salt", "pepper"],
    "grilled cheese":  ["bread", "cheese", "butter"],
 }

pantry_items = ["eggs", "butter", "salt", "pepper", "cheese", "milk", "bread", "garlic"]


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
                ingredient = missing.append(ingredient)

        missing.sort()

        return missing


class Pantry:
    def __init__(self, pantry_items):
        self.ingredients =set(pantry_items)


    def add_ingredients(self,extra_ingredients):
        self.ingredients.update(extra_ingredients)


    def has(self,ingredient):
        if ingredient in self.ingredients:
            return True
        else:
            return False


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
        if recipe.can_make(pantry)is True:
            print(f"{recipe.name: <15} : CAN MAKE ✓")
        else:
            print(f"{recipe.name: <15} : MISSING, {recipe.missing_ingredients(pantry)}")
        
            
  

    all_ingredients.update(recipe.ingredients)
    sorted_ingredients = sorted(all_ingredients)
    print(f"All unique ingredients({len(sorted_ingredients)}) : {sorted_ingredients}")

print(" === RECIPE CHECKER === ")



pantry = Pantry(pantry_items)

recipe= create_recipes(recipe_data)

check_recipes(recipe, pantry.ingredients)













        







        

       

    



