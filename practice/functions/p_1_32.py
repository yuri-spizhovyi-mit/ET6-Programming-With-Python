def calculator(a, operator, b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        try:
            return a / b
        except ZeroDivisionError:
            return "Division by 0 error"
    else:
        return "Unknown operator"


if __name__ == "__main__":
    a_val = input("Enter first value: ")
    operator_val = input("Type operator: ")
    b_val = input("Enter second value: ")
    try:
        result = calculator(float(a_val), operator_val, float(b_val))
        print("Result: ", result)
    except ValueError:
        print("Invalid input")
