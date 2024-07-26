from crypto.Cipher import DES
from crypto.Util.Padding import pad, unpad
from crypto.Random import get_random_bytes


# Function to perform DES encryption
def des_encrypt(plain_text, key):
    # Ensure key is 8 bytes long
    assert len(key) == 8, "Key must be 8 bytes long"
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plain_text.encode(), DES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    return encrypted_text


# Function to perform DES decryption
def des_decrypt(encrypted_text, key):
    # Ensure key is 8 bytes long
    assert len(key) == 8, "Key must be 8 bytes long"
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_padded_text = cipher.decrypt(encrypted_text)
    decrypted_text = unpad(decrypted_padded_text, DES.block_size)
    return decrypted_text.decode()


# Example usage
if __name__ == "__main__":
    key = get_random_bytes(8)  # Generate a random 8-byte key
    plain_text = "Hello, World!"

    print(f"Original text: {plain_text}")
    print(f"Key: {key.hex()}")

    encrypted_text = des_encrypt(plain_text, key)
    print(f"Encrypted text: {encrypted_text.hex()}")

    decrypted_text = des_decrypt(encrypted_text, key)
    print(f"Decrypted text: {decrypted_text}")