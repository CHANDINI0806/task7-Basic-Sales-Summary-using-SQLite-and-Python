import sqlite3

# Connect to SQLite (file will be created if not present)
conn = sqlite3.connect('sales_data.db')
cursor = conn.cursor()

# Create the table
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
''')

# Insert sample sales data
data = [
    ('Apples', 10, 1.5),
    ('Bananas', 5, 1.0),
    ('Oranges', 8, 1.2),
    ('Apples', 6, 1.5),
    ('Bananas', 9, 1.0),
    ('Oranges', 3, 1.2),
    ('Grapes', 12, 2.0),
    ('Pineapples', 4, 3.0),
    ('Mangoes', 7, 1.8),
    ('Strawberries', 15, 2.5)
]

cursor.executemany('INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)', data)

# Commit and close
conn.commit()
conn.close()

print("Database created and sample data inserted.")
