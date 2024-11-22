# Coffee Machine Program

This is a Python-based **Coffee Machine Program** designed to simulate a coffee vending machine. The program allows users to choose from three types of coffee: **Espresso**, **Latte**, and **Cappuccino**, manage resources, handle payments, and issue reports.

---

## Features

### 1. Coffee Menu:
- **Espresso**
  - Ingredients: 50ml water, 18g coffee.
  - Cost: $1.50.
- **Latte**
  - Ingredients: 200ml water, 150ml milk, 24g coffee.
  - Cost: $2.50.
- **Cappuccino**
  - Ingredients: 250ml water, 100ml milk, 24g coffee.
  - Cost: $3.00.

### 2. Resource Management:
- **Track Resources**: The machine keeps track of water, milk, and coffee.
- **Resource Deduction**: Each time a coffee is sold, the corresponding resources are deducted.
- **Resource Check**: The machine ensures there are enough resources to make the selected coffee.

### 3. Payment Handling:
- **Accepts Coins**: The machine allows payment with quarters, dimes, nickels, and pennies.
- **Transaction Validation**: If the inserted money is enough, the transaction is processed, and the change is given.
- **Profit Calculation**: The machine adds the payment to the profit after each successful transaction.

### 4. Commands:
- **`espresso`**: Selects Espresso coffee.
- **`latte`**: Selects Latte coffee.
- **`cappuccino`**: Selects Cappuccino coffee.
- **`report`**: Displays the current resource status and profit.
- **`off`**: Shuts down the coffee machine.

---