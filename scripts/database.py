import sqlite3

DB_PATH = "database/quantum_crypto.db"

def create_database():
    """Creates the database and table if not already existing."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create a table for encrypted data
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS encrypted_data (
        id INTEGER PRIMARY KEY,
        ciphertext TEXT,
        key BLOB
    )
    """)
    conn.commit()
    conn.close()

def store_data(ciphertext, encryption_key):
    """Stores encrypted data in the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO encrypted_data (ciphertext, key) VALUES (?, ?)", (ciphertext, encryption_key))
    conn.commit()
    conn.close()

def retrieve_data():
    """Retrieves the most recent encrypted data from the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT ciphertext, key FROM encrypted_data ORDER BY id DESC LIMIT 1")
    result = cursor.fetchone()
    conn.close()
    return result
