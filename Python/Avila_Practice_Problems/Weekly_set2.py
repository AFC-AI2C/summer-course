# #<!-- ## Problem 5 — Sports Leaderboard
 
# *The season is over and it's time to crunch the numbers. Write a program that processes a list of athletes and generates a leaderboard.*
 
# **You are given the following data:**
 
# <!-- ```python
# athletes = [
#     ("Jordan",  82, 15),   # (name, games_played, goals_scored)
#     ("Patel",   78, 22),
#     ("Okonkwo", 90, 18),
#     ("Li",      65, 9),
#     ("Reyes",   88, 31),
#     ("Fischer", 72, 14),
# ]
# ``` -->
 
# **Your task:**
 
# <!-- - Write a function `goals_per_game(goals, games)` that returns goals per game rounded to 2 decimal places. Return `0.0` if games played is 0.
# - Write a function `mvp_candidate(gpg)` that returns `True` if the rate is 0.25 or higher.
# - Use a `for` loop to process each athlete, call both functions, and print a formatted leaderboard. Use a conditional to mark MVP candidates with a `*`.
# <!-- - After the loop, print the name of the top scorer (most total goals). 



athletes = [
    ("Jordan",  82, 15),   # (name, games_played, goals_scored)
    ("Patel",   78, 22),
    ("Okonkwo", 90, 18),
    ("Li",      65, 9),
    ("Reyes",   88, 31),
    ("Fischer", 72, 14),
]

top_player = ""
total_games= 0
highest_goals = 0


    
def goals_average (games: float, goals: float)->float:
    gpg = goals / games
    if gpg > 0.25:
        return  "Above Average" 
    else:
        return  "Below Average"



print(f"{'Athlete':<12}{'Games Played':<18}{'Goals Scored':<18}{'MVP'}")


for names, games, goals in athletes:
    status = goals_average(games, goals)
    
    if status == "Above Average":
        mvp = "*"
    else:
        mvp = ""
    
    print(f"{names:<12}{games:<18}{goals:<18}{mvp}")

for names, games, goals in athletes:
    if goals > highest_goals:
        highest_goals =goals
        top_player = names
        total_games = games

print(f" The top player: {top_player} with {highest_goals} golas in {total_games} games this season")


for names, games, goals in athletes:
    print(f"{names:<12}{games:<18}{goals:<18}")

