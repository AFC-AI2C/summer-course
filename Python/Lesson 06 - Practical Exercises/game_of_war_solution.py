import random

# Suits and ranks
suits = ["♠", "♣", "♥︎", "♦"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# Rank values
values = {
    "A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
    "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13
}

# Create deck
deck = []
for suit in suits:
    for rank in ranks:
        deck.append((rank, suit))

# Shuffle and deal
random.shuffle(deck)
player_deck = deck[:26]
npc_deck = deck[26:]

player_score = 0
npc_score = 0

print("Game of War Begins!")

while True:

    if len(player_deck) == 0 or len(npc_deck) == 0:
        break

    user_input = input("Enter '+' to play a round or 'exit' to quit: ")

    if user_input == "exit":
        print("Player loses by forfeit!")
        exit()

    if user_input != "+":
        continue

    # Draw cards
    player_card = player_deck.pop(0)
    npc_card = npc_deck.pop(0)

    print(f"{player_card[0]}{player_card[1]}  x  {npc_card[0]}{npc_card[1]}")

    player_value = values[player_card[0]]
    npc_value = values[npc_card[0]]

    # Handle war (ties)
    while player_value == npc_value:
        print("WAR!")

        if len(player_deck) == 0 or len(npc_deck) == 0:
            print("Both players ran out of cards during war!")
            break

        player_card = player_deck.pop(0)
        npc_card = npc_deck.pop(0)

        print(f"{player_card[0]}{player_card[1]}  x  {npc_card[0]}{npc_card[1]}")

        player_value = values[player_card[0]]
        npc_value = values[npc_card[0]]

    # Award point
    if player_value > npc_value:
        print("Player wins this round!")
        player_score += 1
    elif player_value < npc_value:
        print("Opponent wins this round!")
        npc_score += 1

    print(f"Player: {player_score}  |  Opponent: {npc_score}")
    print("-" * 30)

# Game over
print("\nGame Over!")
if player_score > npc_score:
    print("Player wins the game!")
elif npc_score > player_score:
    print("Opponent wins the game!")
else:
    print("The game ends in a tie!")
