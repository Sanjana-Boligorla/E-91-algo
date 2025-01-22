from cryptography.fernet import Fernet

def encrypt_with_key(shared_key, plaintext):
    """
    Encrypts a plaintext using a shared key.
    Args:
        shared_key (int): The quantum key (binary).
        plaintext (str): The message to encrypt.
    Returns:
        ciphertext (bytes): Encrypted data.
        encryption_key (bytes): Symmetric encryption key.
    """
    # Generate a symmetric encryption key
    encryption_key = Fernet.generate_key()
    cipher = Fernet(encryption_key)

    # Encrypt the plaintext
    ciphertext = cipher.encrypt(plaintext.encode())
    return ciphertext, encryption_key

def decrypt_with_key(ciphertext, encryption_key):
    """
    Decrypts the ciphertext using the symmetric encryption key.
    Args:
        ciphertext (bytes): Encrypted data.
        encryption_key (bytes): Symmetric encryption key.
    Returns:
        plaintext (str): Decrypted message.
    """
    cipher = Fernet(encryption_key)
    return cipher.decrypt(ciphertext).decode()
