# Hands-On: Practical Exercises

This repository is designed to reinforce the knowledge already learned in previous lessons and apply it towards practical excerises that can measure learning.


## 🎯 Lesson Objectives

* Create a Calculator
* Build a Card Dealer
* Game of War

---

### Exercise 1: 🧮 Create a Calculator

**Goal**: Write a program that accepts a simple mathematical expression as input, evaluates the expression, and displays the resulting solution to the user. 

✅ *Check*: Output should accept input as two numbers separated by spaces and an operator (eg. `6 - 8`) and the evaulted expression should be printed to the terminal.

---

### Exercise 2: 🂡 Build a Card Dealer

**Goal**: Write a program that contains all 52 standard playing cards in a data structure and when the user instructs the program a random card is dealt to the user, printing it to the screen and removing it from the deck. The program should cycle through all 52 cards before it resets the deck again. User should be able to quit by typing 'exit'.

💩 *Emojidex*: ♠ ♣ ♥︎ ♦

✅ *Check*: User is able to input `+` and screen outputs something like `K♥︎` followed by `A♣` upon another `+` inputted. Typing `exit` results in the program ceasing. 

---

### Exercise 3: ⚔️ Game of War

**Goal**: Somewhat building off of Exercise 2, create a program that randomly deals the player and an NPC an entire deck of cards split between the two of them (for 26 cards each). After the cards are dealt begin a new round each time the user inputs `+` and displaying the top card from each player's deck and awarding a point to the player with the highest numeric card (Ace = 1, King = 13, Queen = 12, Jack = 11). In the case cards of equal value are drawn, both players immediately draw again until one side draws a card of greater numeric value (if both players exhaust their cards no point is awarded to either side and the ultimate winner is announced). Once all cards are exhausted print a message to the screen honoring the winner of the game or announcing a tie. The player can quit the game at any time by typing `exit` whereupon a forfeit is announced. 

💩 *Emojidex*: ♠ ♣ ♥︎ ♦

✅ *Check*: Cards are dealt to the user and an NPC, user is able to input `+` to initiate a round and screen outputs something like `K♥︎  x  6♣` followed by a newline announcing `Player wins this round!`. Scores would be updated each round printing to the screen immediately after the round's result, in this case displaying `Player: 1  | Opponent: 0`. Typing `exit` results in the screen displaying `Player loses by forfeit!` the program ceasing. 

---