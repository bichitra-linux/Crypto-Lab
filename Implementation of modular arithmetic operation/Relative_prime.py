def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def is_relatively_prime(a, b):
    return gcd(a, b) == 1

# Example usage
num1 = 15
num2 = 28

if is_relatively_prime(num1, num2):
    print(f"{num1} and {num2} are relatively prime.")
else:
    print(f"{num1} and {num2} are not relatively prime.")