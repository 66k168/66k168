import sqlite3

def show_alerts():
    conn = sqlite3.connect('data_manager.db')
    cursor = conn.cursor()

    # Check properties that are available
    cursor.execute("SELECT property_id, title FROM properties WHERE availability = 1")
    available = cursor.fetchall()

    if available:
        alerts = ["🏠 Available Properties:"]
        for prop in available:
            alerts.append(f"Property ID: {prop[0]}, Title: {prop[1]}")
        conn.close()
        return alerts
    else:
        conn.close()
        return ["No properties available right now."]
