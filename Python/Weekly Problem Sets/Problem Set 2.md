# Problem Set 2 — Control Flow & Functions
 
**Topics covered:** conditional statements (`if`/`elif`/`else`), `for` loops, `while` loops, functions (`def`, parameters, return values)
 
---
 
## Problem 1 — Pizza Party Planner 🍕
 
*You're organising a pizza party and need to figure out how many pizzas to order. Write a program that helps the host plan for any group size.*
 
**Your task:**
 
- Write a function `pizzas_needed(people, slices_per_person, slices_per_pizza)` that calculates and returns how many whole pizzas to order (always round **up** — you never want to run short!).
- Write another function `leftover_slices(people, slices_per_person, slices_per_pizza` that returns how many slices will be leftover.
- Use input statements to ask how many guests, slices per person, and slices per pizza.
- Using your user defined functions, print the PARTY SUMMARY shown below.

**Example run:**
 
```
=== PIZZA PARTY PLANNER ===
How many guests? 14
Slices per person: 3
Slices per pizza: 8

 
=== PARTY SUMMARY ===
Guests:           14
Pizzas to order:  6
Total slices:     48
Leftover slices:  6
 
```
 
### Challenge
 
Extend `pizzas_needed()` to accept an optional `extra_percent` parameter (default `0`) that adds a percentage buffer to the guest count before calculating — useful for unexpected guests. For example, `extra_percent=10` would plan for 10% more people. Call the function with a 15% buffer and compare the result to the unbuffered version.

```python
from math import ceil

class PizzaParty:
  def __init__(self):
    print("=== PIZZA PARTY PLANNER ===")
    self.num_people = int(input("How many guests? "))
    self.slices_per_person = int(input("Slices per person: "))
    self.slices_per_pizza = int(input("Slices per pizza: "))
    self.extra_percent = int(input("[Optional] Buffer (%): ") or 0)
    self.pizzas_needed = PizzaParty.pizzas_needed(self, self.num_people, self.slices_per_person, self.slices_per_pizza)
    self.leftover_slices = PizzaParty.leftover_slices(self, self.num_people, self.slices_per_person, self.slices_per_pizza)
    self.pizzas_needed_w_buffer = PizzaParty.pizzas_needed_w_buffer(self, self.num_people, self.slices_per_person, self.slices_per_pizza, self.extra_percent)
    print(self)
  #note it would be better for self to be the only input, however this is the way intended to satisfy the instructors
  def pizzas_needed(self: PizzaParty, num_people: int, slices_per_person: int, slices_per_pizza: int) -> int:
    return ceil(num_people * slices_per_person / slices_per_pizza)
  #note it would be better for self to be the only input, however this is the way to satisfy the instructors
  def leftover_slices(self: PizzaParty, num_people: int, slices_per_person: int, slices_per_pizza: int) -> int:
    return slices_per_pizza - (num_people * slices_per_person) % slices_per_pizza
  def pizzas_needed_w_buffer(self: PizzaParty, num_people: int, slices_per_person: int, slices_per_pizza: int, extra_percent: int) -> int:
    return ceil((1 + extra_percent/100) * num_people * slices_per_person / slices_per_pizza)
  def __str__(self):
    text = f"\n=== PARTY SUMMARY ===\n"
    text += f"Guests:             {self.num_people}\n"
    text += f"Pizzas to order:    {self.pizzas_needed}\n"
    text += f"Total slices:       {self.pizzas_needed*self.slices_per_pizza}\n"
    text += f"Leftover slices:    {self.leftover_slices}"
    if self.extra_percent > 0:
      text += f"\n\nExtra guests (%): {self.extra_percent}\n"
      text += f"Guests with extras: {(1+self.extra_percent/100)*self.num_people:.1f}\n"
      text += f"Pizzas to order:    {self.pizzas_needed_w_buffer}\n"
      text += f"Total slices:       {self.pizzas_needed_w_buffer*self.slices_per_pizza}" 
    return text


my_party = PizzaParty()
```

---
 
## Problem 2 — Space Station Oxygen Monitor 🚀
 
*Aboard the ISS, oxygen levels must be continuously monitored. Write a simulation that tracks O2 levels and triggers alerts.*
 
**Your task:**
 
- Write a function `o2_status(level)` that returns:
  - `"CRITICAL"` if level < 15
  - `"LOW"` if level is 15–18
  - `"NORMAL"` if level is 19–23
  - `"HIGH"` if level > 23
- You are given the following hourly O2 readings (as a percentage):
 
- Use a `for` loop to process each reading, call your function, and print the hour and status.
- Use conditionals to print an extra `*** ALERT: TAKE ACTION IMMEDIATELY ***` line whenever the status is `CRITICAL`.
- After the loop, print a summary: how many hours were spent in each status category.
 
**Expected output (partial):**
 
```
Hour  1:  21%  —  NORMAL
Hour  2:  20%  —  NORMAL
Hour  3:  19%  —  NORMAL
Hour  4:  17%  —  LOW
Hour  5:  16%  —  LOW
Hour  6:  14%  —  CRITICAL
*** ALERT: TAKE ACTION IMMEDIATELY ***
...
 
=== STATUS SUMMARY ===
NORMAL:    6 hours
LOW:       3 hours
CRITICAL:  2 hours
HIGH:      1 hour
```
 
### Challenge
 
Add a second function `trend(readings)` that looks at the readings list and returns `"IMPROVING"`, `"DECLINING"`, or `"STABLE"` based on whether the last 3 readings are going up, going down, or neither. Print the trend at the end of the summary.
 
```python
readings = [21, 20, 19, 17, 16, 14, 13, 15, 18, 21, 22, 21]

class SpaceStation():
  def __init__(self, readings):
    self.o2_readings = readings
    self.o2_statuses = []
    for hour, o2_reading in enumerate(self.o2_readings):
      o2_status = SpaceStation.o2_status(self, hour, o2_reading)
      self.o2_statuses.append(o2_status)
      conditional_warning = " *** ALERT: TAKE ACTION IMMEDIATELY ***" * (o2_status == "CRITICAL")
      print(f"Hour {hour+1:>2d}: {o2_reading:>3d}% - {o2_status}" + conditional_warning)
    SpaceStation.trend(self)
    SpaceStation.o2_status_summary(self)
  def o2_status(self, hour: int, level: int) -> str:
    if level < 15:
      return "CRITICAL"
    elif level <= 18:
      return "LOW"
    elif level <= 23:
      return "NORMAL"
    else:
      return "HIGH"
  def o2_status_summary(self):
    text = f"\n=== STATUS SUMMARY ===\n"
    text += f"HIGH:      {sum(o2_status == 'HIGH' for o2_status in self.o2_statuses)} hours\n"  
    text += f"NORMAL:    {sum(o2_status == 'NORMAL' for o2_status in self.o2_statuses)} hours\n"
    text += f"LOW:       {sum(o2_status == 'LOW' for o2_status in self.o2_statuses)} hours\n"
    text += f"CRITICAL:  {sum(o2_status == 'CRITICAL' for o2_status in self.o2_statuses)} hours\n"
    print(text)
  def trend(self):
    print("")
    if self.o2_readings[-3] < self.o2_readings[-2] and self.o2_readings[-2] < self.o2_readings[-1]:
      print("IMPROVING")
    elif self.o2_readings[-3] > self.o2_readings[-2] and self.o2_readings[-2] > self.o2_readings[-1]:
      print("DECLINING")
    else:
      print("STABLE")

my_space_station = SpaceStation(readings)
```
---
 
## Problem 3 — RPG Character Battle ⚔️
 
*You're simulating a turn-based battle between a hero and a monster. Each turn, the hero attacks the monster and then the monster strikes back — until one of them runs out of HP.*
 
**Your task:**
 
- Write a function `attack(defender_hp, damage)` that subtracts damage from defender HP and returns the new HP (minimum 0).
- Write a function `is_alive(hp)` that returns `True` if HP > 0.
- Use a `while` loop to simulate the battle. Each round:
  - The hero deals 18 damage to the monster.
  - If the monster is still alive, it deals 12 damage to the hero.
  - Print the round number and both HP values after each exchange.
  - End the loop when either combatant reaches 0 HP.
- Use conditionals after the loop to print who won.
 
**Starting values:**
```
hero_hp = 100
monster_hp = 90
```
 
**expected output (partial):**
 
```
=== battle start ===
round 1:  hero hp: 88   |  monster hp: 72
round 2:  hero hp: 76   |  monster hp: 54
round 3:  hero hp: 64   |  monster hp: 36
...
hero wins! the monster has been defeated.
```

```python
import random

class Sprite():
  def __init__(self, hp, damage):
    self.hp = hp 
    self.damage = damage
    self.is_alive = Sprite.is_alive(self, hp)
  def is_alive(self, hp):
    if self.hp > 0:
      return True
    else:
      return False
  def attack(self, enemy, defender_hp, damage):
    enemy.hp = max(enemy.hp - self.damage, 0)
    enemy.is_alive = Sprite.is_alive(enemy, enemy.hp)
  def critical_hit(self, enemy, defender_hp, damage):
    if random.randint(1, 10) <= 2:
      hero.is_critical = True
      enemy.hp = max(enemy.hp - self.damage, 0)
      enemy.is_alive = Sprite.is_alive(enemy, enemy.hp) 
    else:
      hero.is_critical = False

class Hero(Sprite):
  pass

class Monster(Sprite):
  pass

class Battle:
  def __init__(self, hero, monster):
    self.round_ = 0
    print("=== BATTLE START ===")
    while (hero.is_alive) and (monster.is_alive):
      self.round_ += 1
      Sprite.attack(hero, monster, monster.hp, hero.damage)
      Sprite.critical_hit(hero, monster, monster.hp, hero.damage)
      if monster.is_alive:
        Sprite.attack(monster, hero, hero.hp, monster.damage)
      print(f"Round {self.round_:2d}:  Hero HP: {hero.hp:3d}    |  Monster HP: {monster.hp:2d}")
      if hero.is_critical:
        print("*** CRITICAL HIT! ***")
    if hero.is_alive:
      print("HERO WINS! The monster has been defeated.")
    else:
      print("MONSTER WINS! The hero has been defeated.")

hero = Hero(hp = 100, damage = 18)
monster = Monster(hp = 90, damage = 12)
battle = Battle(hero, monster)
```

### challenge
 
add a `critical_hit(damage)` function that returns double damage 20% of the time (hint: use `random.randint(1, 10)` — import `random` at the top). apply it to the hero's attack each round and print `*** critical hit! ***` when it triggers.
 
---
 
## problem 4 — mission clearance system 🪖
 
*a soldier must pass a series of automated checks before being cleared for a mission. your program will run each check and produce a final clearance report.*
 
**your task:**
 
define a function for each of the following checks — each should return `true` (cleared) or `false` (denied):
 
```python
def check_fitness(score):
    """cleared if score >= 70."""
 
def check_rank(rank):
    """cleared if rank is 'corporal', 'sergeant', or 'lieutenant'."""
 
def check_service_years(years):
    """cleared if years >= 2."""
```
 
then write a main program that:
- collects the soldier's name, fitness score, rank, and years of service using `input()`.
- uses a `for` loop to run all three checks and store each result.
- uses conditionals to determine overall clearance: the soldier is cleared only if **all three checks pass**.
- prints a full clearance report showing each individual check and the final decision.
 
**example run:**
 
```
soldier name: james okafor
fitness score: 83
rank: corporal
years of service: 3
 
=== MISSION CLEARANCE REPORT ===
Soldier: James Okafor
 
  Fitness check:    PASS
  Rank check:       PASS
  Service check:    PASS
 
FINAL STATUS: CLEARED FOR MISSION.
```
 
### Challenge
 
Store the three check functions in a list of tuples alongside their labels and input values:
 
```python
checks = [
    ("Fitness check", check_fitness, fitness_score),
    ("Rank check", check_rank, rank),
    ("Service check", check_service_years, years),
]
```
 
Then use a single `for` loop to run all checks, print each result, and determine the final clearance — without any repeated `if` statements for individual checks.

```python
class Soldier:
  def __init__(self):
    self.name = input("soldier name: ")
    self.fitness_score = int(input("fitness score: "))
    self.rank = input("rank: ")
    self.tis = int(input("years of service: "))
    self.check_fitness = Soldier.check_fitness(self, self.fitness_score)
    self.check_rank = Soldier.check_rank(self, self.rank)
    self.check_service_years = Soldier.check_service_years(self, self.tis)
    self.checks = [
        ("Fitness check", self.check_fitness, self.fitness_score),
        ("Rank check", self.check_rank, self.rank),
        ("Service check", self.check_service_years, self.tis),
    ]
    self.final_check = Soldier.final_check(self)
    print(self)
  def check_fitness(self, score):
    """cleared if score >= 70."""
    if score >= 70:
      return "PASS"
    else:
      return "FAIL"
  def check_rank(self, rank):
    """cleared if rank is 'corporal', 'sergeant', or 'lieutenant'."""
    if rank.lower() in ['corporal', 'sergeant', 'lieutenant']:
      return "PASS"
    else:
      return "FAIL"
  def check_service_years(self, years):
    """cleared if years >= 2."""
    if years >= 2:
      return "PASS"
    else:
      return "FAIL"
  def final_check(self):
    return (all([check[1] == "PASS" for check in self.checks]))
  def __str__(self):
    text = f"\n=== MISSION CLEARANCE REPORT ===\n"
    text += f"Soldier: {self.name.title()}\n"
    text += f"Fitness check:    {self.check_fitness}\n"
    text += f"Rank check:       {self.check_rank}\n"
    text += f"Service check:    {self.check_service_years}\n\n"
    text += f"FINAL STATUS: {int(1-(self.final_check)) * 'NOT '}CLEARED FOR MISSION."
    return text

james = Soldier()
```
---
 
## Problem 5 — Sports Leaderboard 🏆
 
*The season is over and it's time to crunch the numbers. Write a program that processes a list of athletes and generates a leaderboard.*
 
**You are given the following data:**
 
```python
athletes = [
    ("Jordan",  82, 15),   # (name, games_played, goals_scored)
    ("Patel",   78, 22),
    ("Okonkwo", 90, 18),
    ("Li",      65, 9),
    ("Reyes",   88, 31),
    ("Fischer", 72, 14),
]
```
 
**Your task:**
 
- Write a function `goals_per_game(goals, games)` that returns goals per game rounded to 2 decimal places. Return `0.0` if games played is 0.
- Write a function `mvp_candidate(gpg)` that returns `True` if the rate is 0.25 or higher.
- Use a `for` loop to process each athlete, call both functions, and print a formatted leaderboard. Use a conditional to mark MVP candidates with a `*`.
- After the loop, print the name of the top scorer (most total goals).
 
**Expected output:**
 
```
=== SEASON LEADERBOARD ===
  Athlete       Games   Goals   GPG     MVP?
  ------------------------------------------
  Jordan        82      15      0.18
  Patel         78      22      0.28    *
  Okonkwo       90      18      0.20
  Li            65      9       0.14
  Reyes         88      31      0.35    *
  Fischer       72      14      0.19
 
Top scorer: Reyes (31 goals)
```
 
### Challenge
 
Add a `grade(gpg)` function that returns a letter grade (`A`, `B`, `C`, `D`, or `F`) based on the GPG rate. Define your own grading scale, add the grade to each row, and print a grade distribution summary after the leaderboard using a `for` loop and a dictionary to count grades.
 
---
 
## References
 
- [Python `if` statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
- [Python `for` loops](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Python `while` loops](https://docs.python.org/3/reference/compound_stmts.html#while)
- [Python functions (`def`)](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python `break` and `continue`](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)