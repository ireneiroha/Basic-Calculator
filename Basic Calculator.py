# Step 1: Define operation functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

# Step 2: Map operations to functions in a dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Step 3: Main calculator function
def calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")

        if operation in operations:
            # Step 4: Perform the operation using the dictionary
            result = operations[operation](num1, num2)
            # Step 5: Display the result
            print(f"{num1} {operation} {num2} = {result}")
        else:
            print("Invalid operation. Please enter +, -, *, or /.")
    except ValueError as e:
        print(f"Error: {e}")

# Run the calculator
calculator()