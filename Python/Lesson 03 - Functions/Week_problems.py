
#Problem Set 2 — Control Flow & Functions

#Problem 1 — Pizza Party Planner
#You're organising a pizza party and need to figure out how many pizzas to order. Write a program that helps the host plan for any group size.

#Your task:

#Write a function pizzas_needed(people, slices_per_person, slices_per_pizza) that calculates and returns how many whole pizzas to order (always round up — you never want to run short!).
#Write another function leftover_slices(people, slices_per_person, slices_per_pizza that returns how many slices will be leftover.
#Use input statements to ask how many guests, slices per person, and slices per pizza.
#Using your user defined functions, print the PARTY SUMMARY shown below.

# import math
# party_size = int(input("How many guests are you feeding: "))
# slices_per_person = int(input("How many slice will each person get: "))
# pizza_slices = int(input("How many slices are in the pizza you are ording: "))


# def pizza_needed (size: int, slice: int, pizza_slice: int)-> int:
#     total_slices = size * slice
    
#     total_pizzas_needed = math.ceil(total_slices/ pizza_slice)
    
#     leftover_slices = (pizza_slice * total_pizzas_needed)- total_slices
    
#     padding_for_guest = math.ceil(total_slices * 1.20)
    
#     padding_pizza_count = math.ceil(padding_for_guest/pizza_slice)
    
#     return  total_pizzas_needed, total_slices, leftover_slices, padding_pizza_count

# total_pizzas_needed, total_slices,leftover_slices, padding_pizza_count = pizza_needed(party_size,slices_per_person,pizza_slices)


# header = ("==== Pizza Party Planner ====")
# summary = (" === Party Summary === ")

# print(header)
# print()
# print(f"How many guest: {party_size}")
# print(f"How many slices per person: {slices_per_person}")
# print(f"Slice Per Pizza: {pizza_slices}")
# print()
# print(summary)
# print()
# print(f"Guest: {party_size}")
# print(f"Pizza I need to order: {total_pizzas_needed}")
# print(f"Total Slices that will be served: {total_slices}")
# print(f"Leftover slice of pizza: {leftover_slices}")
# print(f"To be safe we recommend adding a 20% increase in case you have extra guest, order: {padding_pizza_count} Pizzas to be safe")
# print()

# #seq explorer


# for i in range(1,16):
#     print(i, end=" " )
# print()   
# for j in range(2,31,2):
#     print(j, end =" ",)
# print()

# for k in range(20, -1, -2):
#     print(k, end=" ",)
# print()


# st_num = int(input("enter your start number: "))
# sp_num = int(input("enter your stop number: "))
# sr_num = int(input("enter your step number: "))
# def print_range(start: int,stop: int,step:int)->int:
#     for number in range(start, stop, step):
#         print(number, end =" ")


# user_print_range = print_range(st_num,sp_num,sr_num)

# print(user_print_range)


#Problem 3 — Drill Sergeant Fitness Test
#ATTENTION, RECRUIT! The Army Physical Fitness Test is underway. Your program will collect a soldier's performance data and report their results — no excuses accepted.

#Your task:

#Ask the soldier for their name and rank using input().
#Ask how many push-ups they completed and how long their 2-mile run took (in minutes).
#Print a formatted after-action report with their name, rank, and both scores. Also print the soldier's average pace per mile for the run.

# banner = " ====== ATTENTION RECRUIT ====== "

# name = input("What is your name (first, last name): ")
# rank = input("What is your Rank: ")
# pushups = int(input("How many push ups did you complete"))
# run = int(input(""))


#Problem 4 — Road Trip Fuel Calculator
#Write a program that helps a driver estimate the fuel cost for a road trip.

#Ask the user for:

#The distance of the trip in miles
#Their car's fuel efficiency in miles per gallon (MPG)
#The current price of gas per gallon in dollars
#Calculate and print:

#The number of gallons needed (rounded to 2 decimal places)
#The total fuel cost (rounded to 2 decimal places)

# distance = float(input("The distance of the trip in miles: "))
# efficinecy = float(input("What is car's fuel efficiency in miles per gallon (MPG)"))
# gas_price = float(input("What is the current price of gas per gallon in dollars"))

# def road_trip_caculator(dist:float,eff:float,price:float)-> float:
#     gallons_needed = dist / eff 
#     cost = gallons_needed * price
    


#     return gallons_needed, cost

# gallons_needed, total_cost = road_trip_caculator(distance,
#                                efficinecy,
#                                gas_price)




# first_increase = gas_price + .50
# second_increase = gas_price + 1.00
# total_first_increase  =first_increase * gallons_needed
# total_second_increase  = second_increase * gallons_needed

# banner = (" --- Road Trip Cacluator --- ")
# print(banner)
# print(f"Distnace:       {distance}")
# print(f"Fuel efficincy: {efficinecy} MPG")
# print(f"Gas Price:      {gas_price} / gallon")
# print()

# print(f"Total gallons needed: {gallons_needed:.02f}")
# print()

# print(" --- Gas Sernario --- ")
# print(f"Total Fuel cost is gas is: {gas_price} and total is: {total_cost:.02f}")
# print(f"Total Fuel cost is gas is: {first_increase} and total is: {total_first_increase:.02f}")
# print(f"Total Fuel cost is gas is: {second_increase} and total is: {total_second_increase:.02f}")
# print()
# print("===== Projections if Gas Increase ==== ")
# print()
# for increase in[0.0, 0.5, 1.0, 1.5]:
#     new_gas_prices = gas_price + increase
#     total_cost = new_gas_prices * gallons_needed
#     print(f"If gas is: ${new_gas_prices} the total will be: ${total_cost} for your trip. ")



#Aboard the ISS, oxygen levels must be continuously monitored. Write a simulation that tracks O2 levels and triggers alerts.

#Your task:

#Write a function o2_status(level) that returns:
#"CRITICAL" if level < 15
#"LOW" if level is 15–18
# "NORMAL" if level is 19–23
# "HIGH" if level > 23
# You are given the following hourly O2 readings (as a percentage):
# readings = [21, 20, 19, 17, 16, 14, 13, 15, 18, 21, 22, 21]
# Use a for loop to process each reading, call your function, and print the hour and status.
# Use conditionals to print an extra *** ALERT: TAKE ACTION IMMEDIATELY *** line whenever the status is CRITICAL.
# After the loop, print a summary: how many hours were spent in each status category.

# What it is suppossed to look like: 

# Hour  1:  21%  —  NORMAL
# Hour  2:  20%  —  NORMAL
# Hour  3:  19%  —  NORMAL
# Hour  4:  17%  —  LOW
# Hour  5:  16%  —  LOW
# Hour  6:  14%  —  CRITICAL
# *** ALERT: TAKE ACTION IMMEDIATELY ***
# ...
 
# === STATUS SUMMARY ===
# NORMAL:    6 hours
# LOW:       3 hours
# CRITICAL:  2 hours
# HIGH:      1 hour


# reading_list = [21, 20, 19, 17, 16, 14, 13, 15, 18, 21, 22, 21]




# def O2_reading_status (level):
#     if level < 15:
#         return "Critical"
#     elif level <= 18:
#         return "Low"
#     elif level <= 23:
#         return "Normal"
#     else:
#         return "High"

# critical_count = 0
# low_count = 0
# normal_count = 0
# high_count = 0
    

# print("====== Hour Break Down of Readings ======")
# print()
# print()
# for hour in range(1,13):
#     reading= reading_list[hour -1]
#     status = O2_reading_status(reading)
    
#     print(f"Hour {hour}: {reading}%  -- {status}")
#     if status == "Critical":
#         critical_count += 1
#         print(" *** ALERT: TAKE ACTION IMMEDIATELY *** ")
#     elif status == "Low":
#         low_count += 1
#     elif status == "Normal":
#         normal_count += 1
#     else:
#         high_count += 1
# print()
# print()
# print(f"========== STATUS SUMMARY ============")
# print()
# print(f"Crtical Status Count: {critical_count} Hours")
# print(f"Low Status Count:     {low_count} Hours")
# print(f"Normal Status Count:  {normal_count} Hours")
# print(f"High Status Count:    {high_count} Hours")


#Problem 3 — RPG Character Battle 
# You're simulating a turn-based battle between a hero and a monster. 
# Each turn, the hero attacks the monster and then the monster strikes back — until one of them runs out of HP.

# Your task:

# Write a function attack(defender_hp, damage) that subtracts damage from defender HP and returns the new HP (minimum 0).
# Write a function is_alive(hp) that returns True if HP > 0.
# Use a while loop to simulate the battle. Each round:
# The hero deals 18 damage to the monster.
# If the monster is still alive, it deals 12 damage to the hero.
# Print the round number and both HP values after each exchange.
# End the loop when either combatant reaches 0 HP.
# Use conditionals after the loop to print who won.
# Starting values:

# hero_hp = 100
# monster_hp = 90
# Expected output (partial):

# === BATTLE START ===
# Round 1:  Hero HP: 88   |  Monster HP: 72
# Round 2:  Hero HP: 76   |  Monster HP: 54
# Round 3:  Hero HP: 64   |  Monster HP: 36
# ...
# HERO WINS! The monster has been defeated.


############ come back to this one is confusing ################################3

# def attack(defender_healthpoints, damage):
#     new_def_healthpoints = defender_healthpoints - damage
    
#     return max(0, new_def_healthpoints)


# def alive(healthpoints):
#     if healthpoints > 0:
#         return True



# count = 1


# hero_healthpoints = 100
# monster_healthpoints = 90
# monster_damage = 18
# hero_damage = 12

# while hero_healthpoints > 0:
#     count += 1
#     if monster_healthpoints > 0 :
#         monster_healthpoints 

############################################################################





def check_fitness(score)-> bool:
    if score >= 70:
        print("PASS")
        return True
    else:
        return False


 
def check_rank(rank)-> bool:
    if rank == 'Corporal' or rank == 'Sergeant' or rank == 'Lieutenant':
        print("PASS")
        return True
    else:
        return False
    

 
def check_service_years(years) -> bool:
    if years >= 2:
        print("PASS")
        return True
    else:
        return False

soldiers = []
while True:

    name = input("Enter your first and last name: ").upper()
    fitness_score = int(input("Enter your Fintess Score:  "))
    rank = input("Enter your full rank, ('Corporal', 'Sergeant', 'Lieutenant' or ' Other '): ").upper()
    tis = int(input("Enter your years in service: "))

    soldiers.append({
        "name" : name,
        "fitness" : fitness_score,
        "rank" : rank,
        "serivce" : tis
    })

    another_input = input("Do you want to enter another Soldier (Y/N): ").upper()

    if another_input == "N":
        break

for soldier in soldiers:
    fitness_check =  check_fitness(soldier["fitness"])
    rank_check = check_rank(soldier["rank"])
    tis_check = check_service_years(soldier["service"])
                   
    overall_check = (check_fitness(fitness_score)
    and check_rank(rank)
    and check_service_years(tis) )



    if overall_check:
        print()
        print("Soldiers Inforamation")
        print(f"Soldier Name:     {name} ")
        print(f"Fitness Score:    {fitness_score} ")
        print(f"Rank:             {rank}")
        print(f"Years in Service: {tis} ")
        print()
        print(" === MISSION CLEARANCE REPORT === ")
        print()
        print(f"Soldier: {name}")
        print(f"    Fitness Check: {'PASS' if fitness_check else 'fail'} ")
        print(f"    Rank check   : {'PASS' if rank_check else 'fail'} ")
        print(f"    Service Check: {'PASS' if tis_check else 'fail'} ")
        print()
        print("FINAL STATUS: CLEARED FOR MISSION.")


    else:
        print("Service Memeber did not meet standard")
        print(f"Name: {name} ")
        print(f"Rank: {rank}")





