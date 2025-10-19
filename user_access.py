import sqlite3

# ------------------ Create Employees Table ------------------
def create_table():
    conn = sqlite3.connect('data_manager.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            role TEXT CHECK(role IN ('Admin','Viewer')),
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# ------------------ Sample Employee ------------------
def add_sample_employee():
    conn = sqlite3.connect('data_manager.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR IGNORE INTO employees (employee_id, name, email, role, password)
        VALUES (?, ?, ?, ?, ?)
    ''', (1, "Admin User", "admin@agadir.com", "Admin", "1234"))
    conn.commit()
    conn.close()

# ------------------ Login Function ------------------
# ------------------ Login Function (accept any email/password) ------------------
def login(email, password):
    # Return a dummy user tuple as if it exists in DB
    # (id, name, email, role, password)
    return (0, "Dev User", email, "Admin", password)


# ------------------ Add New Employee ------------------
def add_employee(name, email, role, password):
    conn = sqlite3.connect('data_manager.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO employees (name, email, role, password)
        VALUES (?, ?, ?, ?)
    ''', (name, email, role, password))
    conn.commit()
    conn.close()

# ------------------ Get All Employees ------------------
def get_employees():
    conn = sqlite3.connect('data_manager.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Run once to create table
create_table()
