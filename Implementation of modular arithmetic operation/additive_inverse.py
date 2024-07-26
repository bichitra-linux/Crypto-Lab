def additive_inverse(num, modulus):
    inverse = modulus - num
    return inverse % modulus

# Example usage
num = 7
modulus = 10
inverse = additive_inverse(num, modulus)
print(f"The additive inverse of {num} modulo {modulus} is {inverse}.")