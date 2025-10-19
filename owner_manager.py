import sqlite3
from datetime import date

# Add a new owner
def add_owner(name, email, phone):
    conn = sqlite3.connect('data_manager.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO owners (name, email, phone, joined_date)
        VALUES (?, ?, ?, ?)
    ''', (name, email, phone, date.today()))
    conn.commit()
    conn.close()

# Get all owners
def get_owners():
    conn = sqlite3.connect('data_manager.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM owners")
    rows = cursor.fetchall()
    conn.close()
    return rows
