import sqlite3
from datetime import date

# ------------------ Create table if not exists ------------------
def create_table():
    conn = sqlite3.connect('data_manager.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS owners (
            owner_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT,
            joined_date DATE
        )
    ''')
    conn.commit()
    conn.close()

# ------------------ Add sample owner ------------------
def add_sample_owners():
    conn = sqlite3.connect('data_manager.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR IGNORE INTO owners (owner_id, name, email, phone, joined_date)
        VALUES (?, ?, ?, ?, ?)
    ''', (1, "Owner 1", "owner1@test.com", "0612345678", date.today()))
    conn.commit()
    conn.close()

# ------------------ Functions ------------------
def add_owner(name, email, phone):
    conn = sqlite3.connect('data_manager.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO owners (name, email, phone, joined_date)
        VALUES (?, ?, ?, ?)
    ''', (name, email, phone, date.today()))
    conn.commit()
    conn.close()

def get_owners():
    conn = sqlite3.connect('data_manager.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM owners")
    rows = cursor.fetchall()
    conn.close()
    return rows

# ------------------ Run on import ------------------
create_table()
add_sample_owners()
