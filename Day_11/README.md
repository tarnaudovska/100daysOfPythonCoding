## 🎲🃏 Blackjack game with Functions (with outputs) and Dictionaries

Welcome to the **Blackjack Game**! This program is written in Python and uses **functions**, **dictionaries**, and interactive **inputs/outputs** to simulate the popular casino game of Blackjack.

## 🛠 Features
- Player vs. Dealer gameplay.
- Deck of cards implemented using **dictionaries**.
- Real-time scoring to determine winner.

## 🧩 How It Works
1. **Start the Game**: The player and dealer are dealt two cards each.
2. **Gameplay**:
   - Player can `Hit` to draw another card or `Stand` to hold.
   - Dealer follows predefined rules (e.g., must hit if score < 17).
3. **Determine Winner**: The program calculates scores and declares a winner.

## 🔑 Key Code Features
- **Functions**: 
  - `add_cards()`: Draws a card randomly from the deck.
  - `user_score()`: shows the score of the player or the dealer.
- **Dictionaries**: The player and the dealer have both nested dictionaries with the delt cards and the scores.
<pre>
game = {
    "player":{
      "cards":[],
      "score":0,
    },
    "computer":{
      "cards":[],
      "score":0,
    }
  }
</pre>