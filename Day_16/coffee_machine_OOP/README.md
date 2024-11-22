# OOP ☕ Coffee Machine ☕

This project implements an object-oriented coffee machine in Python. The coffee machine allows users to choose from a selection of drinks, make payments, and manage resources such as water, coffee, and milk. The program uses several classes to model the machine, the menu, and the money handling. The goal is to simulate a real-world coffee machine with the ability to manage ingredients, handle payments, and prepare coffee.

---

## Components

### 1. **Classes**
The program is structured using Object-Oriented Programming (OOP) principles, with multiple classes that interact with each other:

- **`Menu`**: This class handles the menu items and allows users to view available drinks and find a specific drink by name.
- **`MenuItem`**: This class represents a single menu item (i.e., a drink) with details like name, cost, and required ingredients.
- **`CoffeeMaker`**: This class is responsible for checking if enough resources are available to prepare a coffee and making the coffee.
- **`MoneyMachine`**: This class manages the payment process, including accepting coins, verifying if the correct amount is inserted, and issuing change.

### 2. **Program Flow**
The main flow of the program is interactive and runs in a loop until the user decides to turn off the coffee machine.

#### Main Loop:
- The user is prompted to choose a coffee or enter specific commands (e.g., `report` or `off`).
- If the user chooses a coffee, the program checks if sufficient resources are available (using the `CoffeeMaker` class). If resources are sufficient and the user has inserted enough money (checked by the `MoneyMachine` class), the coffee is prepared.
- If the user types `report`, the system provides a report showing the current status of ingredients and profits.

