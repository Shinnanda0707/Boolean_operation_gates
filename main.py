from basic_gates import or_gate, and_gate, not_gate


# Declare XOR gate
def xor_gate(input_1: bool, input_2: bool) -> bool:
    # Set variable x to (input_1 or input_2)
    x = or_gate(input_1, input_2)

    # Set variable y to not(input_1 and input_2)
    y = and_gate(input_1, input_2) # y = input_1 or input_2
    y = not_gate(y) # y = not(input_1 and input_2)

    # Calculate the result
    result = and_gate(x, y)

    return result


# Input a, b and print a XOR b
a = int(input("Input a (0 or 1): "))
b = int(input("Input b (0 or 1): "))
print(f"a XOR b = {int(xor_gate(bool(a), bool(b)))}")
