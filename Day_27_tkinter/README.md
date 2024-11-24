# Basic GUI Program with Tkinter

## Overview
This project demonstrates a simple GUI (Graphical User Interface) application built with Python's `tkinter` module. The application features:
- A label that displays text.
- A button that updates the label's text with user input.
- An entry box for text input.

---

## Features
1. **Label**: Displays dynamic text that can be updated by user input.
2. **Button**: Triggers actions when clicked (e.g., updating the label with input from the user).
3. **Entry**: Accepts user input.

---

## How It Works
1. The program starts with a window titled **"My first GUI program"**.
2. A default label is displayed, initially showing "Label".
3. Users can type into the entry box.
4. Clicking the **"Click Me"** button updates the label with the text entered in the entry box.

---

## Code Breakdown

### Creating the Main Window
```python
from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
