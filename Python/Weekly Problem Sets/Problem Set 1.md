# Problem Set 1 — Python Basics

**Topics covered:** `print()`, `range()`, `type()`, `input()`, type casting (`int()`, `float()`, `str()`, `bool()`)

---

## Problem 1 — Introduction Card

Write a program that asks the user for their **name** and their **favorite number**, then prints a personalized card using `print()`.

Your output should look something like this (content will vary based on input):

```
*******************************
*  Hello, Ryan!               *
*  Your favorite number is 7  *
*******************************
```

**Requirements:**
- Use `input()` to collect the name and favorite number
- Use `print()` to display the card with a border made of `*` characters
- The border of '*' characters should always be based on the length of the favorite number line

**Advanced:**
Use `type()` to print the data type of the name and the favorite number as collected from `input()`. Then use type casting to convert the favorite number to an `int` and a `float`, and print those converted values along with their types. Your output should look like:

```
Raw input type: <class 'str'>
As int: 7  -->  <class 'int'>
As float: 7.0  -->  <class 'float'>
```

```python
def intro_card() -> None:
    usr_name = input("Enter your name: ")
    usr_fav = input("Enter your favorite number: ")
    lines = []
    lines.append(f"Hello, {usr_name}!")
    lines.append(f"Your favorite number is {usr_fav}")
    line_lens = [len(line) for line in lines]
    print("*"*(2*3+max(line_lens)))
    print(f"*  {lines[0]:<{max(line_lens)}}  *")
    print(f"*  {lines[1]:<{max(line_lens)}}  *")
    print("*"*(2*3+max(line_lens)))
    print(f"Raw input type: {type(usr_fav)}")
    print(f"As int: {int(usr_fav)}  -->  {type(int(usr_fav))}")
    print(f"As float: {float(usr_fav)}  -->  {type(float(usr_fav))}")

intro_card()
```

---

## Problem 2 — Sequence Explorer

Use `range()` to print each of the following sequences. Each sequence should be printed on a single line, with values separated by spaces.

1. All integers from **1 to 15** (inclusive)
2. All **even** numbers from **2 to 30** (inclusive)
3. A **countdown** from **20 down to 0**, counting by 2s

**Example output for sequence 1:**
```
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
```

> Hint: Look into the `end` parameter of `print()` and the `step` argument of `range()`.

**Advanced:**
Ask the user to enter a **start**, **stop**, and **step** value. Use `input()` to collect these, then use `range()` to print the resulting sequence on one line.

```python
def seq_explrr() -> None:
    usr_start_1 = int(input("Enter start number: "))
    usr_stop_1 = int(input("Enter stop number: "))
    print(*[x for x in range(usr_start_1,usr_stop_1+1)], sep=" ")
    usr_start_2 = int(input("Enter start number: "))
    usr_stop_2 = int(input("Enter stop number: "))
    print(*[x for x in range(usr_start_2,usr_stop_2+1,2) if x % 2 ==0], sep=" ")
    usr_start_3 = int(input("Enter countdown start number: "))
    usr_stop_3 = int(input("Enter countdown stop number: "))
    usr_step_3 = int(input("Enter step number: "))
    print(*[x for x in range(usr_start_3,usr_stop_3-1,-usr_step_3)], sep=" ")

seq_explrr() 
```
---

## Problem 3 — Drill Sergeant Fitness Test
 
*ATTENTION, RECRUIT! The Army Physical Fitness Test is underway. Your program will collect a soldier's performance data and report their results — no excuses accepted.*
 
**Your task:**

- Ask the soldier for their name and rank using `input()`.
- Ask how many push-ups they completed and how long their 2-mile run took (in minutes).
- Print a formatted after-action report with their name, rank, and both scores. Also print the soldier's average pace per mile for the run.
 
> **Note:** `input()` always returns a *string*. You will need to convert numbers before doing any arithmetic.
 
**Example run:**
 
```
ENTER SOLDIER NAME: John Baker
ENTER RANK: Private
PUSH-UPS COMPLETED: 42
2-MILE RUN TIME (minutes): 16
 
=== AFTER-ACTION REPORT ===
Soldier: Private John Baker
Push-ups: 42
2-mile run: 16.0 minutes
Average pace: 8.0 minutes per mile
DISMISSED.
```
---

```python
class Soldier:
    def __init__(self):
        self.name = input("ENTER SOLDIER NAME: ")
        self.rank = input("ENTER RANK: ")
        self.pu = input("PUSH-UPS COMPLETED: ")
        self.runtime = input("2-MILE RUN TIME (minutes): ")
    def fit_tst(self) -> None:
        print("=== AFTER-ACTION REPORT ===")
        print(f"Soldier: {self.rank} {self.name}")
        print(f"Push-ups: {self.pu}")
        print(f"2-mile run: {float(self.runtime)} minutes")
        print(f"Average pace: {float(self.runtime)/2:.1f} minutes per mile")
        print("DISMISSED.")

usr = Soldier()
usr.fit_tst()


### See below for LLM feedback about a more pythonic solution
class Soldier:
    def __init__(self, name: str, rank: str, push_ups: int, runtime: float):
        self.name = name
        self.rank = rank
        self.push_ups = push_ups
        self.runtime = runtime
    @property
    def average_pace(self) -> float:
        """Calculates the average pace per mile over a 2-mile run."""
        return self.runtime / 2
    def __str__(self) -> str:
        """Defines how the Soldier object is represented as a string (the report)."""
        return (
            f"=== AFTER-ACTION REPORT ===\n"
            f"Soldier: {self.rank} {self.name}\n"
            f"Push-ups: {self.push_ups}\n"
            f"2-mile run: {self.runtime:.1f} minutes\n"
            f"Average pace: {self.average_pace:.1f} minutes per mile\n"
            f"DISMISSED."
        )

# --- External Input Handling (Keeps the class clean) ---
if __name__ == "__main__":
    # Gather inputs outside the class
    name = input("ENTER SOLDIER NAME: ")
    rank = input("ENTER RANK: ")    
    # Safely convert types immediately
    push_ups = int(input("PUSH-UPS COMPLETED: ") or 0)
    runtime = float(input("2-MILE RUN TIME (minutes): ") or 0.0)
    # Instantiate the clean object
    usr = Soldier(name, rank, push_ups, runtime)
    # Print the report cleanly using the __str__ representation
    print("\n" + str(usr))
```

## Problem 4 — Road Trip Fuel Calculator

Write a program that helps a driver estimate the fuel cost for a road trip.

Ask the user for:
1. The **distance** of the trip in miles
2. Their car's **fuel efficiency** in miles per gallon (MPG)
3. The current **price of gas** per gallon in dollars

Calculate and print:
- The number of gallons needed (rounded to 2 decimal places)
- The total fuel cost (rounded to 2 decimal places)

**Example output:**
```
--- Road Trip Fuel Estimate ---
Distance:        350 miles
Fuel efficiency: 28 MPG
Gas price:       $3.45 / gallon

Gallons needed:  12.5
Total fuel cost: $43.13
```

**Requirements:**
- Use `input()` for all three inputs
- Cast inputs to `float` using `float()`
- Use `print()` with clear labels for all output values

**Advanced:**
Extend the program to also calculate the cost for **3 different gas price scenarios** using `range()`:
- The price the user entered
- That price plus $0.50
- That price plus $1.00

Print all three estimates in a table. Use `range()` to loop through the three scenarios rather than writing three separate calculations.

```
--- Price Scenarios ---
Gas @ $3.45/gal:  Total = $43.13
Gas @ $3.95/gal:  Total = $49.38
Gas @ $4.45/gal:  Total = $55.63
```
```python
class RoadTrip:
    def __init__(self, dist: float, fuel_eff: float, price_gal: float):
        self.dist = dist
        self.fuel_eff = fuel_eff
        self.price_gal = price_gal
    @property
    def gal_ndd(self) -> float:
        """Calculates the number of gallons needed given distance and fuel efficiency."""
        return self.dist / self.fuel_eff
    @property
    def total_price(self) -> float:
        """Calculates the total cost of gas given fuel needed and price per gallon."""
        return self.gal_ndd * self.price_gal
    @property
    def price_scenarios(self) -> str:
        """Calculates the total cost of gas given fuel needed and 3 different gas price scenarios"""
        output_scenarios = ""
        for i in range(0, 3, 1):
            scnr_per_gal = self.price_gal + i * 0.5
            scnr_tot = scnr_per_gal * self.gal_ndd
            output_scenarios += f"Gas @ ${scnr_per_gal:.2f}/gal:  Total = ${scnr_tot:.2f}\n"
        return output_scenarios
    def __str__(self) -> str:
        """Defines how the RoadTrip object is represented as a string (the report)."""
        return (
            f"\n--- Road Trip Fuel Estimate ---\n"
            f"Distance:        {self.dist} miles\n"
            f"Fuel efficiency: {self.fuel_eff} MPG\n"
            f"Gas price:       ${self.price_gal:.02f} / gallon\n"
            f"\n"
            f"Gallons needed:  {self.gal_ndd:.2f}\n"
            f"Total fuel cost: ${self.total_price:.02f}\n"
            f"\n--- Price Scenarios ---\n"
           f"{self.price_scenarios}"
        )

if __name__ == "__main__":
    dist = float(input("ENTER DISTANCE (miles): ") or 0)
    fuel_eff = float(input("ENTER FUEL EFFICIENCY (mpg): ") or 1)
    price_gal = float(input("ENTER GAS PRICE ($/gal): ") or 1)
    trip = RoadTrip(dist, fuel_eff, price_gal)
    print(trip)
```
---

## References

- [Python `print()` documentation](https://docs.python.org/3/library/functions.html#print)
- [Python `range()` documentation](https://docs.python.org/3/library/stdtypes.html#range)
- [Python `type()` documentation](https://docs.python.org/3/library/functions.html#type)
- [Python `input()` documentation](https://docs.python.org/3/library/functions.html#input)
- [Python Built-in Types](https://docs.python.org/3/library/stdtypes.html)
