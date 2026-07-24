import random



games_list = [1,3,5,7,9]

games_played = int(input("How many games do you want to play( 1-9) odd number only: "))
########### to make them pick a odd number by the list ##############

while games_played not in games_list:
    print("Invalid choice.")
    games_played = int(input("Please enter 1, 3, 5, 7, or 9: "))


user_wins = 0
comp_wins = 0
wins_needed = (games_played //2)+ 1



while user_wins < wins_needed and comp_wins < wins_needed:
    
    com_choice = random.choice(["rock","paper", "scissors"]).upper()

    user_input = input("Lets play a game enter (Rock, Paper or Scissors) : ").upper()
    

    
    
    if user_input not in ["ROCK", "PAPER", "SCISSORS"]:
        print("invaild response")
        print("please tyr again")
        print(f" User: {user_wins} Computer Win: {comp_wins}")
        continue

    elif com_choice == user_input:
        print("Tied")
        print("Please try again")
        print(f" User: {user_wins} Computer Win: {comp_wins}")
        continue

    elif com_choice == "ROCK" and user_input == "PAPER":
        print("You Won")
        user_wins += 1
        print(f" User: {user_wins} Computer Win: {comp_wins}")
        

    elif com_choice == "ROCK" and user_input == "SCISSORS":
        print("You Lost")
        comp_wins +=1
        print(f" User: {user_wins} Computer Win: {comp_wins}")

    elif com_choice == "PAPER" and user_input == "SCISSORS":
        print("You Won")
        user_wins += 1
        print(f" User: {user_wins} Computer Win: {comp_wins}")
        

    elif com_choice == "PAPER" and user_input == "ROCK":
        print("You Lost")
        comp_wins +=1
        print(f" User: {user_wins} Computer Win: {comp_wins}")

    elif com_choice == "SCISSORS" and user_input == "ROCK":
        print("You Won")
        user_wins += 1
        print(f" User: {user_wins} Computer Win: {comp_wins}")
        

    elif com_choice == "SCISSORS" and user_input == "PAPER":
        print("You Lost")
        comp_wins +=1
        print(f" User: {user_wins} Computer Win: {comp_wins}")
        



if user_wins == wins_needed:
    print(f" Congradulation you won this match.   User: {user_wins} Computer Win: {comp_wins}")

else:
    print(f" Sorry better luck next time the Computer won this match.   User: {user_wins} Computer Win: {comp_wins}")


#########Come back to work on this #############################



# def compound_intrest(princple:float, intrest_rate:float, time_in_years:float, n: int = 1 ) -> float:
#     return princple * (1+ intrest_rate/n) ** (n*time_in_years)

# # This one works better and is cleaner####
# def compound_interest(
#     principal: float,
#     interest_rate: float,
#     years: float,
#     compounds_per_year: int = 1,
# ) -> float:
    
#     return principal * (1 + interest_rate / compounds_per_year) ** (compounds_per_year * years)
    

# print(f"The Compount Intrest is $: {compound_intrest(1000,0.0061, 10, 1):.2f}")

########### complete ##################################

############################################################






