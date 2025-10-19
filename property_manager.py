import sqlite3
from datetime import date

# Add a property
def add_property(owner_id, title, address, type_, price, availability=True):
    conn = sqlite3.connect('data_manager.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO properties (owner_id, title, address, type, price_per_night, availability, added_date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (owner_id, title, address, type_, price, availability, date.today()))
    conn.commit()
    conn.close()

# Get all properties
def get_properties():
    conn = sqlite3.connect('data_manager.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM properties")
    rows = cursor.fetchall()
    conn.close()
    return rows
