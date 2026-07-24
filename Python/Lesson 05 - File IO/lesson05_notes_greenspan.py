import random
class RockPaperScissors():
    def __init__(self):
        self.rcp_user = input("Enter (R)ock, (P)aper, or (S)cissors: ")
        while not(self.validate_RCP(self.rcp_user)):
            self.rcp_user = input("Enter (R)ock, (P)aper, or (S)cissors: ") 
        self.rcp_cpu = random.choice(["rock","paper","scissors"])
        self.rcp_user_reduced = self.reduce_RCP(self.rcp_user)
        self.outcome = self.determine_outcome()
        self.rcp_internal = {   "rcp_user": self.rcp_user, 
                                "rcp_user_reduced": self.rcp_user_reduced, 
                                "rcp_cpu": self.rcp_cpu,
                                "outcome": self.determine_outcome()
                            }    
        print(self)
    @staticmethod
    def validate_RCP(input_):
        return True if input_.lower() in ["r","p", "s", "rock", "paper", "scissors"] else False
    @staticmethod
    def reduce_RCP(input_):
        if (input_.lower() in ["r", "rock"]) == True:
            return "rock"
        elif (input_.lower() in ["p", "paper"]) == True:
            return "paper"
        elif (input_.lower() in ["s", "scissors"]) == True:
            return "scissors"
    def __str__(self):
        return f"User: {self.reduce_RCP(self.rcp_user):<8} Cpu: {self.rcp_cpu:<12} Outcome: {self.outcome}"
    def determine_outcome(self):
        if self.rcp_user_reduced == "rock":
            if self.rcp_cpu == "paper":
                return "Lose"
            elif self.rcp_cpu == "scissors":
                return "Win"
        elif self.rcp_user_reduced == "paper":
            if self.rcp_cpu == "scissors":
                return "Lose"
            elif self.rcp_cpu == "rock":
                return "Win"
        elif self.rcp_user_reduced == "scissors":
            if self.rcp_cpu == "rock":
                return "Lose"
            elif self.rcp_cpu == "paper":
                return "Win"
        return "Tie"

#a = RockPaperScissors()
#a.rcp_internal["outcome"]

class BestOf():
    def __init__(self):
        self.total_games = int(input("Enter best of (number between 1 and 9): "))
        while( (self.total_games in [1,3,5,7,9]) == False ):
            self.total_games = int(input("Enter best of (number between 1 and 9): "))
        self.wins_needed = (self.total_games // 2) + 1
        self.history = []
        self.games_played = len(self.history)
        self.user_wins = sum(outcome == "Win" for outcome in self.history)
        self.cpu_wins = sum(outcome == "Lose" for outcome in self.history)
        while self.games_played < self.total_games and self.user_wins < self.wins_needed and self.cpu_wins < self.wins_needed:
            self.competition = RockPaperScissors()
            if self.competition.outcome != "Tie":
                self.history.append(self.competition.outcome)
                self.user_wins = sum(outcome == "Win" for outcome in self.history)
                self.cpu_wins = sum(outcome == "Lose" for outcome in self.history)    
                self.games_played = len(self.history)
        if self.user_wins == self.wins_needed:
            print(f"You win the best of {self.total_games}!")
        elif self.cpu_wins == self.wins_needed:
            print(f"You lose the best of {self.total_games}!")
        else:
            print(f"You tied the best of {self.total_games}!")

a = BestOf()

import math
def compound_interest(P, r, t, n=1):
    return math.floor((P * (1 + r / n) ** (n * t))*100)/100

compound_interest(1000, 0.0061, 10, 1)
compound_interest(1000, 0.0031, 10, 1)
compound_interest(1000, 0.07, 10, 1)

#Manipulating files
#'r' read, 'w' write, 'a' append
# with (open('input.txt', 'rw')) as file:
#     lines = file.readlines()
#     for line in lines:
#         print(line)

# with (open('input.txt', 'w')) as file:
#     lines = file.readlines()
#     for text in text_to_write:
#         file.write(text)

# f.writelines(lines)

import random
with open('output.txt','w') as file:
    for i in range(100):
        file.write(str(random.randint(50,100)) + "\n")

numbers = []
minimum = 100
maximum = 0
sum_numbers = 0
counter = 0
with open('output.txt','r') as file:
    lines = file.readlines()
    for line in lines:
        number = int(line.replace("\n",""))
#    for line.strip() in lines:
#        number = int(line)
        numbers.append(number)
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number
        counter += 1
        sum_numbers += number

print(f"Min: {minimum}\t Max: {maximum}\t Average: {sum_numbers/counter}")


#examples
import os
os.environ.get("HOME")

#os.getcwd()
#os.chdir()
#os.mkdir()
#os.makedirs()
import pathlib
p = pathlib.Path(os.getcwd())
type(p)
#p.mkdir()