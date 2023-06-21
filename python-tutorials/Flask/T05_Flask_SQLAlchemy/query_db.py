import sqlite3
from app import User, app

# Connect to the SQLite database
conn = sqlite3.connect("db.sqlite3")
c = conn.cursor()

# Query the sqlite_master table for a list of all tables
c.execute("SELECT name FROM sqlite_master WHERE type='table'")

# Fetch the results
tables = c.fetchall()

# Print the results
print("--Tables--")
for table in tables:
    print(table[0])

# Execute a SELECT query
c.execute("SELECT * FROM User")

# Fetch the results
results = c.fetchall()

# Print the results
print("--Results--")
for row in results:
    print(row)
    
# Close the database connection
conn.close()
