#TODO FINISH IMPLEMENTATION / CHECK STRUCTURE COMPLIES WITH REQUIREMENTS.

import sqlite3

DB_PATH = "database/portfolio.db"

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Allows accessing columns by name
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stocks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            stock_ticker TEXT UNIQUE NOT NULL,
            stock_name TEXT NOT NULL,
            current_shares REAL NOT NULL,
            purchase_price REAL NOT NULL,
            current_price REAL NOT NULL,
            purchase_date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()  # Run this once to initialize the DB
