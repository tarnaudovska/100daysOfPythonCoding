# U.S. States Game 🗺️

## Overview
The **U.S. States Game** is an interactive Python project where users test their knowledge of U.S. states by identifying them on a map. The game uses the `turtle` module for displaying the map and `pandas` for handling state data.
---
## Preview
<img src="preview/preview.jpg" alt="Quiz Interface" width="300px">


## How It Works
1. The program displays a blank map of the United States.
2. Users are prompted to input the name of a U.S. state.
3. Correct guesses are displayed on the map.
4. The game continues until the user identifies all 50 states or types **"Exit"**.

---

## Features
- Displays a visual map of the U.S.
- Tracks correctly guessed states and displays them on the map.
- Allows the user to exit the game early and displays missing states in red on the map.
- Uses the `turtle` module for graphical output and `pandas` for data manipulation.

---

## File Requirements
1. **Input CSV File**:  
   The `50_states.csv` file contains the state names and their coordinates on the map.  
   Example structure:
   ```csv
   state,x,y
   Alabama,139,-77
   Alaska,-203,-180
   ...
