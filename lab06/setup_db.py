import sqlite3
import os

DB_NAME = "users.db"

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS users")

cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    login TEXT NOT NULL,
    role TEXT NOT NULL
)
""")

users_data = [
    (1, "ivan_user", "student"),
    (2, "olena_user", "student"),
    (3, "test_user", "guest"),
    (4, "admin_hidden", "administrator")
]

cursor.executemany(
    "INSERT INTO users VALUES (?, ?, ?)",
    users_data
)

conn.commit()
conn.close()

print("База створена:", os.path.abspath(DB_NAME))
