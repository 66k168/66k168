import sqlite3
from datetime import date

# Add a booking
def add_booking(property_id, customer_name, check_in, check_out, total_amount):
    conn = sqlite3.connect('data_manager.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO bookings (property_id, customer_name, check_in, check_out, total_amount, booked_date)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (property_id, customer_name, check_in, check_out, total_amount, date.today()))
    conn.commit()
    conn.close()

# Get all bookings
def get_bookings():
    conn = sqlite3.connect('data_manager.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bookings")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Update a booking
def update_booking(booking_id, total_amount):
    conn = sqlite3.connect('data_manager.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE bookings
        SET total_amount = ?
        WHERE booking_id = ?
    ''', (total_amount, booking_id))
    conn.commit()
    conn.close()

# Delete a booking
def delete_booking(booking_id):
    conn = sqlite3.connect('data_manager.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM bookings WHERE booking_id = ?", (booking_id,))
    conn.commit()
    conn.close()

# Create table if it doesn't exist
def create_table():
    conn = sqlite3.connect('data_manager.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
            property_id INTEGER,
            customer_name TEXT NOT NULL,
            check_in DATE NOT NULL,
            check_out DATE NOT NULL,
            total_amount REAL CHECK(total_amount >= 0),
            booked_date DATE DEFAULT (DATE('now')),
            FOREIGN KEY(property_id) REFERENCES properties(property_id)
        )
    ''')
    conn.commit()
    conn.close()

# Run once to ensure table exists
create_table()

