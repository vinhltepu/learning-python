import os
import sqlite3

DB_NAME = os.path.join(os.path.dirname(__file__), "shop.db")

def connect():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def create_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        code TEXT NOT NULL UNIQUE,
        price REAL NOT NULL DEFAULT 0,
        stock INTEGER NOT NULL DEFAULT 0
    );
    """)

    conn.commit()
    conn.close()
