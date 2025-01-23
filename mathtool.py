from llama_index.core.tools import FunctionTool
#fun
def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
def reverse_number(n: int) -> int:
    reversed_number = int(str(abs(n))[::-1]) * (-1 if n < 0 else 1)
    return reversed_number

def sum_of_digits(n: int) -> int:
    digit_sum = sum(int(digit) for digit in str(abs(n)))
    return digit_sum
# Wrap functions in FunctionTool
add_tool = FunctionTool.from_defaults(
    fn=add,
    name="Add",
    description="Adds two numbers. Usage: add(a, b)"
)

subtract_tool = FunctionTool.from_defaults(
    fn=subtract,
    name="Subtract",
    description="Subtracts the second number from the first. Usage: subtract(a, b)"
)

multiply_tool = FunctionTool.from_defaults(
    fn=multiply,
    name="Multiply",
    description="Multiplies two numbers. Usage: multiply(a, b)"
)

divide_tool = FunctionTool.from_defaults(
    fn=divide,
    name="Divide",
    description="Divides the first number by the second. Usage: divide(a, b)"
)
reverse_tool = FunctionTool.from_defaults(
    fn=reverse_number,
    name="reverse_number",
    description="reverse the given number. Usage: reverse_number(n)"
)

sum_of_digits_tool = FunctionTool.from_defaults(
    fn=sum_of_digits,
    name="sum_of_digits",
    description="sum of digits of the given number. Usage: sum_of_digits(n)"
)
