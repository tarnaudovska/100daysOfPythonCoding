# Hangman Game 🎮
## Functions, Code Blocks and While Loops

Exercise: Hangman game (guess the word)  
<pre>
  +---+  
  |   |  
  O   |  
 /|\  |  
 / \  |  
      |  
_e___a__a__
</pre>

This repository contains a Python implementation of the classic **Hangman** game. Players attempt to guess a randomly chosen word by guessing one letter at a time before running out of lives.

---

## 📝 Features

- **Random Word Selection**: Words are randomly chosen from a predefined list in the `hangman_words.py` file.
- **Visual Feedback**: A "stages" ASCII art from `hangman_art.py` visually represents the player's progress and remaining lives.
- **Player Feedback**: Alerts when:
  - A guessed letter is already used.
  - A guessed letter is not in the word (losing a life).
  - The player wins or loses.
- **Dynamic Word Display**: Updates guessed letters in the word while showing blanks for unguessed ones.

---
