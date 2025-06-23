import sqlite3

# Connect to (or create) the database file
conn = sqlite3.connect("sample_database.db")
cursor = conn.cursor()

# Create a sample table
cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT,
    amount_spent INTEGER,
    purchase_date TEXT
)
''')

# Insert some sample records
cursor.executemany('''
    INSERT INTO users (id, name, city, amount_spent, purchase_date)
    VALUES (?, ?, ?, ?, ?)
''', [
    (1, 'Alice', 'Delhi', 12000, '2025-05-01'),
    (2, 'Bob', 'Mumbai', 8000, '2025-05-05'),
    (3, 'Charlie', 'Pune', 9500, '2025-06-01')
])

# Save and close
conn.commit()
conn.close()

print("✅ sample_database.db created successfully!")
