def logic_gate_simulator(A, B=None, gate_type="AND"):
    """
    Simulates basic logic gates (AND, OR, NOT, XOR, NAND, NOR).

    Args:
        A (int): First input (0 or 1).
        B (int, optional): Second input (0 or 1). Required for gates other than NOT.
        gate_type (str): Type of gate ("AND", "OR", "NOT", "XOR", "NAND", "NOR").

    Returns:
        int: Output of the logic gate (0 or 1).
    """
    # Normalize gate_type to uppercase once
    gate_type = gate_type.upper()

    # Ensure A and B are valid Boolean values
    if A not in [0, 1] or (B is not None and B not in [0, 1]):
        raise ValueError("Inputs A and B must be 0 or 1.")

    # Logic gate simulation
    if gate_type == "AND":
        return A & B  # Bitwise AND
    elif gate_type == "OR":
        return A | B  # Bitwise OR
    elif gate_type == "NOT":
        return 1 - A  # Logical NOT (negation of A)
    elif gate_type == "XOR":
        return A ^ B  # Exclusive OR
    elif gate_type == "NAND":
        return 1 - (A & B)  # Negated AND
    elif gate_type == "NOR":
        return 1 - (A | B)  # Negated OR
    else:
        raise ValueError(
            f"Invalid gate type: {gate_type}. Supported gates: AND, OR, NOT, XOR, NAND, NOR."
        )


# Test cases
if __name__ == "__main__":
    print("Running Test Cases...")

    # Test cases for all gate types
    test_cases = [
        {"A": 0, "B": 0, "gate_type": "AND", "expected": 0},
        {"A": 0, "B": 1, "gate_type": "AND", "expected": 0},
        {"A": 1, "B": 0, "gate_type": "AND", "expected": 0},
        {"A": 1, "B": 1, "gate_type": "AND", "expected": 1},
        {"A": 0, "B": 0, "gate_type": "OR", "expected": 0},
        {"A": 0, "B": 1, "gate_type": "OR", "expected": 1},
        {"A": 1, "B": 0, "gate_type": "OR", "expected": 1},
        {"A": 1, "B": 1, "gate_type": "OR", "expected": 1},
        {"A": 0, "B": None, "gate_type": "NOT", "expected": 1},
        {"A": 1, "B": None, "gate_type": "NOT", "expected": 0},
        {"A": 0, "B": 0, "gate_type": "XOR", "expected": 0},
        {"A": 0, "B": 1, "gate_type": "XOR", "expected": 1},
        {"A": 1, "B": 0, "gate_type": "XOR", "expected": 1},
        {"A": 1, "B": 1, "gate_type": "XOR", "expected": 0},
        {"A": 0, "B": 0, "gate_type": "NAND", "expected": 1},
        {"A": 0, "B": 1, "gate_type": "NAND", "expected": 1},
        {"A": 1, "B": 0, "gate_type": "NAND", "expected": 1},
        {"A": 1, "B": 1, "gate_type": "NAND", "expected": 0},
        {"A": 0, "B": 0, "gate_type": "NOR", "expected": 1},
        {"A": 0, "B": 1, "gate_type": "NOR", "expected": 0},
        {"A": 1, "B": 0, "gate_type": "NOR", "expected": 0},
        {"A": 1, "B": 1, "gate_type": "NOR", "expected": 0},
    ]

    # Run the test cases
    for i, case in enumerate(test_cases, 1):
        A, B, gate_type, expected = (
            case["A"],
            case["B"],
            case["gate_type"],
            case["expected"],
        )
        result = logic_gate_simulator(A, B, gate_type)
        assert result == expected, (
            f"Test Case {i} Failed: {case} → Got {result}, Expected {expected}"
        )
        print(f"Test Case {i} Passed: {case} → Result: {result}")

    print("All test cases passed successfully!")
