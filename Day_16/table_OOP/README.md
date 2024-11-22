# Pokémon Table Example using PrettyTable

This is an example of how to create a simple table using the `PrettyTable` Python module. The table contains information about three Pokémon characters and their types.

## Python Code:

```python
from prettytable import PrettyTable

# Create a table
table = PrettyTable()

# Add columns to the table
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# Align the columns to the left
table.align = "l"

# Print the table
print(table)
