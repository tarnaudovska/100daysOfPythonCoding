def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

# Take input from the user
user_input = input("Enter your calculation (e.g., 25+110): ")

# Extract the numbers and operator
for operator in operations.keys():
    if operator in user_input:
        n1, n2 = user_input.split(operator)
        n1, n2 = int(n1), int(n2)  # Convert to integers
        operation = operations[operator]
        result = operation(n1, n2)
        print(f"{n1} {operator} {n2} = {result}")
        break