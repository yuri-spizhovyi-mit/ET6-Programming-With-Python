def logic_gate_simulator(a: int, b: int, gate_type: str = "AND") -> int:
    if gate_type == "AND":
        return a & b
    elif gate_type == "OR":
        return a | b
    elif gate_type == "NOT":
        return 1 - a
    elif gate_type == "XOR":
        return a ^ b
    elif gate_type == "NAND":
        return 1 - (a & b)
    elif gate_type == "NOR":
        return 1 - (a | b)
    else:
        raise ValueError(
            f"Invalid gate type: {gate_type}. Supported gates: AND, OR, NOT, XOR, NAND, NOR."
        )


if __name__ == "__main__":
    a = input("Enter a value for a (0 or 1): ")
    b = input("Enter a value for b (0 or 1): ")
    gate_type = input("Enter the gate type (AND or OR): ")
    a = int(a)
    b = int(b)
    result = logic_gate_simulator(a, b, gate_type)
    print(f"Result of {gate_type} gate for inputs a={a}, b={b}: result = {result}")
