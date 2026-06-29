import sqlite3


def init_db():
    connection = sqlite3.connect("zeroday.db")
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS debts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    balance REAL,
    interest_rate REAL,
    minimum_payment REAL
)
    """)
    connection.commit()
    connection.close()
