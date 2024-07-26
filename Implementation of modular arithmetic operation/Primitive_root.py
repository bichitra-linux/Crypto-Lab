from math import factorize

def is_primitive_root(g, p):
    """
    Check if g is a primitive root modulo p.
    """
    if pow(g, p-1, p) != 1:
        return False

    factors = factorize(p-1)
    for factor in factors:
        if pow(g, (p-1)//factor, p) == 1:
            return False

    return True

def find_primitive_root(p):
    """
    Find a primitive root modulo p.
    """
    for g in range(2, p):
        if is_primitive_root(g, p):
            return g

    return None

# Example usage
p = 23
primitive_root = find_primitive_root(p)
if primitive_root is not None:
    print(f"A primitive root modulo {p} is: {primitive_root}")
else:
    print(f"No primitive root found modulo {p}")