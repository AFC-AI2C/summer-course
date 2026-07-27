# Problem Set 3 — Importing Modules

**Topics covered:** `import` statements, the `random` module, the `math` module, the `turtle` module

---

## Problem 1 — Dice Roll Simulator 🎲

*You're building a virtual dice table for a tabletop war game. Soldiers roll dice to determine attack outcomes, movement, and morale checks.*

**Your task:**

- Import the `random` module.
- Write a function `roll(sides)` that simulates rolling a single die with the given number of sides and returns the result. Use `random.randint()`.
- Write a function `roll_many(num_dice, sides)` that rolls multiple dice and returns a list of results.
- Simulate the following scenario:
  - Roll **2d6** (two 6-sided dice) for a movement check. Print each roll and the total.
  - Roll **1d20** for an attack check. If the result is 20, print `CRITICAL HIT!`. If it's 1, print `CRITICAL MISS!`. Otherwise print the result.
  - Roll **3d8** for damage. Print each roll, the total, and the average (rounded to 1 decimal place).
- Run the damage roll **1000 times** using a `for` loop and track the average total damage across all runs. Print the result — how close is it to the theoretical average?

> **Hint:** The theoretical average of one d8 is 4.5, so three d8s should average around 13.5.

**Example output (results will vary):**

```
=== MOVEMENT CHECK (2d6) ===
Roll 1: 4   Roll 2: 6   Total: 10

=== ATTACK CHECK (1d20) ===
Roll: 20 — CRITICAL HIT!

=== DAMAGE ROLL (3d8) ===
Rolls: [5, 3, 7]   Total: 15   Average: 5.0

=== SIMULATION (1000 damage rolls) ===
Simulated average total: 13.47
Theoretical average:     13.5
```

```python
import math, random
def roll(sides):
    return random.randint(1, sides)

def roll_many(num_dice, sides):
    return [roll(sides) for dice in range(num_dice)]

def roll_stats(rolls_list):
    return {'average': math.floor( sum(rolls_list)/len(rolls_list) * 10) / 10 , 'total': sum(rolls_list)}

def is_crit(roll):
    if roll == 20:
        return 'CRITICAL HIT!'
    elif roll == 1:
        return 'CRITICAL MISS!'
    else:
        return roll

#movement 
r = roll_many(2,6)
print(r, roll_stats(r))

#attack check
print(is_crit(roll(20)))

#damage
r = roll_many(3,6)
print(r, roll_stats(r))

#damage loop
total_history = []
for i in range(1000):
    r = roll_many(3,8)
    total_history.append(roll_stats(r)['total'])

print(f'The mean of sample totals of three die (n = 1000) is {math.floor(sum(total_history)/len(total_history) * 100) / 100}.')
```

### Challenge

Use `random.seed(42)` at the top of your program and run it twice. Notice that the results are identical both times — explain in a comment why this happens and when it might be useful. Then remove the seed and use `random.choice()` to pick a random battle quote from a list of at least five strings and print it at the end.

---

## Problem 2 — Space Mission Calculator 🚀

*Your spacecraft navigation system needs precise calculations. Import the `math` module to power the nav computer.*

**Your task:**

- Import the `math` module.
- Write a function `distance(x1, y1, x2, y2)` that calculates the straight-line distance between two points in space using the distance formula. Use `math.sqrt()`.
- Write a function `orbit_circumference(radius)` that calculates the circumference of a circular orbit. Use `math.pi`.
- Write a function `fuel_needed(mass, velocity)` that calculates kinetic energy as `0.5 * mass * velocity ** 2`, then returns the result rounded to 2 decimal places using `math.floor()`.
- Use the functions to print a navigation report for the following mission data:

```python
ship_pos    = (0, 0)
station_pos = (143, 892)
orbit_radius = 6371        # km (Earth's radius)
ship_mass    = 50000       # kg
ship_velocity = 7800       # m/s
```

- Also print `math.log(ship_velocity, 10)` and explain in a comment what this value represents.

**Expected output:**

```
=== NAVIGATION REPORT ===
Distance to station:    902.35 units
Orbit circumference:    40030.17 km
Kinetic energy (fuel):  1520100000000.0 J
Log10 of velocity:      3.89
```

```python
import math
def distance(x1, y1, x2, y2):
    return math.sqrt( (x1-x2)**2 + (y1-y2)**2 )

def orbit_circumference(radius):
    return math.pi * 2 * radius

def fuel_needed(mass, velocity):
    return math.floor( 0.5 * mass * velocity ** 2 * 100) / 100

ship_pos    = (0, 0)
station_pos = (143, 892)
orbit_radius = 6371        # km (Earth's radius)
ship_mass    = 50000       # kg
ship_velocity = 7800       # m/s

distance(*ship_pos, *station_pos)

print(f'=== NAVIGATION REPORT ===')
print(f'Distance to station:    {distance(*ship_pos, *station_pos):.02f} units')
print(f'Orbit circumference:    {orbit_circumference(orbit_radius):.02f} km')
print(f'Kinetic energy (fuel):  {fuel_needed(ship_mass, ship_velocity):.02f} J')
print(f'Log10 of velocity:      {math.log(ship_velocity, 10):.02f}')
```

### Challenge

Use `math.degrees()` and `math.radians()` to write a function `bearing(x1, y1, x2, y2)` that returns the angle in degrees from one point to another using `math.atan2()`. Print the bearing from the ship to the station. Then use `math.ceil()` and `math.floor()` on the distance result and explain the difference between them in a comment.

---

## Problem 3 — Animal Habitat Drawing 🐢

*Use Python's `turtle` module to draw a nature scene — a simple habitat with a sun, grass, and a pond.*

**Turtle basics — read this first:**

The `turtle` module lets you draw by moving a virtual "pen" around the screen. Here are the key commands you'll need:

```bash
#this block is not necessary
#python -m venv venv_problem_set_3
#source ./venv_problem_set_3/bin/activate
#python --version
#pip install turtle
#pip list
#pip freeze
#pip freeze >> requirements.txt
#deactivate
#echo "venv_problem_set_3" >> .gitignore
#git status
#pip list
#pip install -r .\requirements.txt
#pip list
```

```python
import turtle
t = turtle.Turtle()       # create a turtle to draw with
t.forward(100)            # move forward 100 pixels
t.right(90)               # turn right 90 degrees
t.left(90)                # turn left 90 degrees
t.penup()                 # lift the pen (move without drawing)
t.pendown()               # put the pen down (start drawing)
#t.goto(x, y)              # jump to a specific position
t.color("green")          # set the pen color
t.begin_fill()            # start filling a shape
t.end_fill()              # fill the shape with the current color
t.circle(50)              # draw a circle with radius 50
#turtle.done()             # keep the window open when finished
```

**Your task:**

- Draw a simple outdoor scene containing all of the following:
  - A **yellow sun** in the upper corner (use `t.circle()` with a fill color).
  - A green **grass strip** along the bottom of the screen (a filled rectangle).
  - A **blue pond** (a filled circle or oval) sitting on the grass.
  - At least **3 trees** drawn using a `for` loop — each tree should be a brown rectangle (trunk) topped with a green circle (leaves). Use `t.penup()` / `t.pendown()` and `t.goto()` to space them out.

- Use `t.speed(0)` to make the drawing fast.
- Organise your code with at least two functions, e.g. `draw_sun(t, x, y)` and `draw_tree(t, x, y)`.

> **Note:** The turtle window may open behind other windows — check your taskbar if you don't see it.

**Expected result:** A simple nature scene with a sun, grass, a pond, and a row of trees.

```python
import turtle
t = turtle.Turtle()       # create a turtle to draw with
t.screen.bgcolor('#2afad4')
t.speed(0)

#yellow sun
t.penup()                 # lift the pen (move without drawing)
t.goto(775, 100)             # jump to a specific position
t.pendown()               # put the pen down (start drawing)
t.color("yellow")          # set the pen color
t.fillcolor('yellow')
t.begin_fill()            # start filling a shape
t.circle(250)             # draw a circle with radius 250
t.end_fill()              # fill the shape with the current color

#green grass
t.penup()                 # lift the pen (move without drawing)
t.goto(-1000, -150)             # jump to a specific position
t.pendown()               # put the pen down (start drawing)
t.color('#6db409')          # set the pen color
t.fillcolor('#6db409')
t.begin_fill()            # start filling a shape
t.forward(2000)            # move forward 100 pixels
t.right(90)               # turn right 90 degrees
t.forward(350)
t.right(90)
t.forward(2000)
t.right(90)
t.forward(350)
t.end_fill()              # fill the shape with the current color

#tree
for i in range(3):
    #tree trunk
    x_offset = 175
    y_scaler = 1.1
    tree_height = 75
    t.penup()                 # lift the pen (move without drawing)
    t.goto(-800 + i*x_offset, -125)             # jump to a specific position
    t.pendown()               # put the pen down (start drawing)
    t.color("brown")          # set the pen color
    t.fillcolor('brown')
    t.begin_fill()            # start filling a shape
    t.right(90)
    t.forward(20)            # move forward 100 pixels
    t.right(90)               # turn right 90 degrees
    t.forward(75 * y_scaler * (i+1)**1.25)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(75 * y_scaler * (i+1)**1.25)
    t.end_fill()              # fill the shape with the current color
    #tree leaves
    t.penup()                 # lift the pen (move without drawing)
    tree_tops = (-740, -530, -340)
    t.goto(tree_tops[i], -125)             # jump to a specific position
    t.pendown()               # put the pen down (start drawing)
    my_colors = ('green','#b46d09','#ec2910')
    t.color(my_colors[i])          # set the pen color
    t.fillcolor(my_colors[i])             #
    t.begin_fill()            # start filling a shape
    circle_sizes = (50,80,100)
    t.circle(circle_sizes[i])             # draw a circle with radius 50
    t.end_fill()              # fill the shape with the current color    

#pond
for x in range(512,587):
    t.penup()                 # lift the pen (move without drawing)
    t.goto(x, -310)             # jump to a specific position
    t.pendown()               # put the pen down (start drawing)
    my_color = 'blue'
    t.color(my_color)          # set the pen color
    t.fillcolor(my_color)             #'#32a8a4'
    t.begin_fill()            # start filling a shape
    t.circle(75)             # draw a circle with radius 50
    t.end_fill()              # fill the shape with the current color
```

### Challenge

Add a `for` loop that uses `random.randint()` to place **10 trees** at random x-positions along the grass line, each with a randomly chosen height between 40 and 100 pixels. Import `random` alongside `turtle` to make this work. Make sure no tree is drawn off-screen by clamping the x-position within a safe range.

---

## Problem 4 — Animal Guessing Game 🐾

*Combine `random` and `math` to build a number-guessing game with a twist — the computer gives hints using math.*

**Your task:**

- Import `random` and `math`.
- Randomly generate a **secret number** between 1 and 100 using `random.randint()`. The player must guess it.
- Use a `while` loop to keep accepting guesses. After each wrong guess, print a hint:
  - Use `math.fabs()` to calculate the absolute distance between the guess and the secret number.
  - If the distance is > 40, print `ICE COLD`.
  - If the distance is > 20, print `COLD`.
  - If the distance is > 10, print `WARM`.
  - Otherwise print `HOT!`
- When the player guesses correctly, print the number of guesses it took, and use `math.log2()` to print the "information-theoretic" minimum guesses needed (i.e. `math.ceil(math.log2(100))`). Add a comment explaining what this number means.

**Example run:**

```
=== ANIMAL GUESSING GAME ===
A secret animal is waiting...

Guess a number (1-100): 50
Hint: COLD

Guess a number (1-100): 25
Hint: WARM

Guess a number (1-100): 18
Hint: HOT!

Guess a number (1-100): 21
CORRECT! The secret animal was: narwhal
You guessed it in 4 tries.
Minimum possible guesses (optimal): 7
```

### Challenge

Track all the player's guesses in a list. After the game ends, use `math.fsum()` to calculate the sum of all guesses and print the mean guess.


## Problem 5 — Square Spiral 🌀
 
*Use the `turtle` module to draw a square spiral. The more times around the square, the tighter and more impressive the spiral.*
 
**How a square spiral works:**
 
A normal square has 4 sides of equal length. A spiral is made the same way, except the side length gets a little longer each time you draw a side. After many iterations this creates an expanding square spiral pattern.
 
```
side length starts at some value
each side: draw forward, turn right 90 degrees
after each full loop of 4 sides: the side length has grown
```
 
**Your task:**
 
- Ask the user how many times they want to go around the square using `input()`. Cast it to an `int`.
- Use a `for` loop to draw the spiral. The total number of sides drawn is `laps * 4` (4 sides per loop). Each lap should:
  - Move the turtle forward by the current side length.
  - Turn right by 90 degrees.
  - Increase the side length by a small fixed amount (try `5` to start).
- Use `t.speed(0)` to draw quickly.
- Use `turtle.done()` to keep the window open when finished.
 
> **Hint:** Start with a side length of `10`. After each side, add `5`. With 10 laps that's 40 sides drawn, growing from length 10 up to 205.
 
**Example run:**
 
```
How many times around the square? 10
```
 
*Result: A square spiral that expands outward, completing 10 full rotations.*
 
### Challenge
 
Ask the user for a second input: a color mode. If they type `"rainbow"`, change the pen color on every side using `t.color()` and a list of colors cycled with the modulo `%` operator. If they type a specific color name like `"blue"`, draw the whole spiral in that color. Use a conditional to handle both cases.
 
 ---
 
## References
 
- [Python `random` module](https://docs.python.org/3/library/random.html)
- [Python `math` module](https://docs.python.org/3/library/math.html)
- [Python `turtle` module](https://docs.python.org/3/library/turtle.html)
- [Turtle graphics beginner guide](https://docs.python.org/3/library/turtle.html#turtle-methods)
 
---