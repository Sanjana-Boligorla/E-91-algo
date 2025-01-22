from scripts.key_generation import generate_quantum_key
from scripts.encryption import encrypt_with_key, decrypt_with_key
from scripts.database import create_database, store_data, retrieve_data

def main():
    # Step 1: Set up the database
    create_database()

    # Step 2: Generate quantum keys using E91 protocol
    alice_key, bob_key = generate_quantum_key()
    print(f"Alice's Key: {alice_key}, Bob's Key: {bob_key}")

    # Step 3: Encrypt a plaintext message
    plaintext = "QuantumSecureMessage"
    ciphertext, encryption_key = encrypt_with_key(alice_key, plaintext)
    print(f"Ciphertext: {ciphertext}")

    # Step 4: Store encrypted data in the database
    store_data(ciphertext, encryption_key)
    print("Data stored in database.")

    # Step 5: Retrieve and decrypt the data
    retrieved_ciphertext, retrieved_key = retrieve_data()
    decrypted_plaintext = decrypt_with_key(retrieved_ciphertext, retrieved_key)
    print(f"Decrypted Plaintext: {decrypted_plaintext}")

if __name__ == "__main__":
    main()
