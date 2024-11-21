# Number Guessing Game 🎯

Welcome to the **Number Guessing Game**! Test your luck and logic by trying to guess a randomly chosen number within a limited number of attempts. Choose your difficulty level and see if you can outsmart the game!

## 🛠 Features
- Three difficulty levels: **Easy**, **Normal**, and **Hard**.
- Randomly generated number between 0 and 25 for each game session.
- Feedback for every guess (e.g., "Too High" or "Too Low").
- Dynamic attempts based on the chosen difficulty.

## 🔧 How to Play
1. **Start the Game**: Run the script and input `y` to begin.
2. **Choose Difficulty**:
   - **Easy**: 15 attempts
   - **Normal**: 10 attempts
   - **Hard**: 5 attempts
3. **Guess the Number**: Input your guess (between 0 and 25). The game will guide you by telling you if your guess is too high or too low.
4. **Win or Lose**:
   - Win by guessing the correct number before running out of attempts.
   - Lose when all attempts are used up.

## 📜 Code Highlights
- **Random Number Generation**: `random.randint(0, 25)` is used to generate the target number.
- **Difficulty Levels**: A dictionary (`levels`) maps difficulty levels to the number of attempts.
- **Feedback Loop**: Nested loops manage attempts and feedback for user guesses.


## 🚀 Run the Game
1. Clone this repository: Day_11

Enjoy the game, and good luck guessing! 🤞