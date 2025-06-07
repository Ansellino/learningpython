class DivideByZeroError(Exception):
    def __init__(self, message="Division by zero is not allowed"):
        super().__init__(message)

def divide_numbers(a, b):
    if b == 0:
        raise DivideByZeroError("Cannot divide by zero")
    return a / b

try:
    result = divide_numbers(10, 0)
except DivideByZeroError as e:
    print(f"Error: {e}")

"""
Output:
Error: Cannot divide by zero
"""