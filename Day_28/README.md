# 🍅 Pomodoro Timer Application

## Overview

This is a **Pomodoro Timer** built using Python's `tkinter` library. It is designed to implement the Pomodoro Technique, a time management method that alternates work sessions with short and long breaks to improve productivity.

## Features

- **Work Timer**: Set to 25 minutes by default.
- **Short Break Timer**: Set to 5 minutes by default.
- **Long Break Timer**: Set to 20 minutes by default.
- **Cycle Management**: Automatically alternates between work sessions, short breaks, and long breaks after every four work sessions.
- **Reset Functionality**: Allows you to reset the timer and all progress.
- **Visual Indicators**:
  - A ✔ symbol appears after each completed work session.
  - Dynamic labels update to show whether it's a work session or break time.

---

## Code Breakdown

### 1. **Constants**
- `PINK`, `RED`, `GREEN`, and `YELLOW`: Define UI color scheme.
- `WORK_MIN`, `SHORT_BREAK_MIN`, and `LONG_BREAK_MIN`: Specify the duration of work and break sessions in minutes.

### 2. **UI Setup**
- **`Tkinter` Components**:
  - `Label`: Displays the current timer state (Work, Break) and session progress.
  - `Canvas`: Displays a tomato image and the timer countdown.
  - `Button`: Start and Reset buttons to control the timer.
- Background colors and font styles are set for a visually appealing interface.

### 3. **Timer Mechanism**
- **`timer_start()`**:
  - Tracks the session type (work, short break, or long break) based on the `reps` counter.
  - Calls `count_down()` with the appropriate duration.
- **`count_down()`**:
  - Manages the countdown in minutes and seconds.
  - Updates the timer display every second using `window.after()`.
  - Handles session transitions and updates progress markers (`✔`).

### 4. **Reset Mechanism**
- **`timer_reset()`**:
  - Stops the ongoing timer.
  - Resets the `reps` counter and UI elements to their initial state.

---

## Usage Instructions

1. **Run the Program**:
   - Ensure Python is installed along with the `tkinter` library.
   - Save the provided code in a Python file (e.g., `pomodoro.py`) and run it.

2. **Start the Timer**:
   - Click the "Start" button to begin the first work session.

3. **Take Breaks**:
   - The timer will alternate between work and break sessions automatically.

4. **Reset the Timer**:
   - Click the "Reset" button to stop the timer and clear progress.

---

## File Requirements

- `tomato.png`: Place the tomato image in the specified path (`./Day_28/tomato.png`) for the UI.
- Python libraries required:
  - `tkinter`
  - `math`


