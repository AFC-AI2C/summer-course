# ## Problem 1 — Dice Roll Simulator 🎲

# *You're building a virtual dice table for a tabletop war game. Soldiers roll dice to determine attack outcomes, movement, and morale checks.*

# **Your task:**

# - Import the `random` module.
# - Write a function `roll(sides)` that simulates rolling a single die with the given number of sides and returns the result. Use `random.randint()`.
# - Write a function `roll_many(num_dice, sides)` that rolls multiple dice and returns a list of results.
# - Simulate the following scenario:
#   - Roll **2d6** (two 6-sided dice) for a movement check. Print each roll and the total.
#   - Roll **1d20** for an attack check. If the result is 20, print `CRITICAL HIT!`. If it's 1, print `CRITICAL MISS!`. Otherwise print the result.
#   - Roll **3d8** for damage. Print each roll, the total, and the average (rounded to 1 decimal place).
# - Run the damage roll **1000 times** using a `for` loop and track the average total damage across all runs. Print the result — 

import random

def roll(sides):
    return random.randint(1,sides)

def roll_many(num_dice, sides):
    rolls = []

    for i in range(num_dice):
        rolls.append(roll(sides))

    return rolls

print(roll(6))
print(roll_many(2, 6))
print(roll_many(1, 20))
print(roll_many(3, 8))

movement = roll_many(2, 6)

print("Movement Rolls:", movement)
print("Total Movement:", sum(movement))

attack = roll(20)

if attack == 20:
    print(f"Roll: {attack} — CRITICAL HIT!")
elif attack == 1:
    print(f"Roll: {attack} — CRITICAL MISS!")
else:
    print(f"Roll: {attack}")
print()



damage_rolls = roll_many(3, 8)
total = sum(damage_rolls)
average = total / len(damage_rolls)
print(f"Rolls: {damage_rolls}   Total: {total}   Average: {average:.1f}")

total_damage = 0

for i in range(1000):

    damage_rolls = roll_many(3,8)

    total_damage += sum(damage_rolls)

average_damage = total_damage / 1000

print(f"Average Total Damage: {average_damage:.2f}")


