def mix_columns(state):
    # Define the fixed matrix for the MixColumns operation
    matrix = [
        [0x02, 0x03, 0x01, 0x01],
        [0x01, 0x02, 0x03, 0x01],
        [0x01, 0x01, 0x02, 0x03],
        [0x03, 0x01, 0x01, 0x02]
    ]

    # Create a new state matrix to store the result
    new_state = [[0 for _ in range(4)] for _ in range(4)]

    # Perform the MixColumns operation
    for col in range(4):
        for row in range(4):
            for i in range(4):
                new_state[row][col] ^= multiply(matrix[row][i], state[i][col])

    return new_state

def multiply(a, b):
    # Perform the multiplication in the Galois field GF(2^8)
    result = 0
    for _ in range(8):
        if b & 1:
            result ^= a
        a <<= 1
        if a & 0x100:
            a ^= 0x11B
        b >>= 1
    return result