import sqlite3

# connect to database or create if not found
conn = sqlite3.connect("db.sqlite")

# create a cursor
cursor = conn.cursor()

# only has 5 data types
# NULL
# INTEGER
# REAL
# TEXT
# BLOB


# create a table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS customers (
    first_name TEXT,
    last_name TEXT,
    email TEXT
    )
    """
)

# insert into table
cursor.execute(
    """
    INSERT INTO customers VALUES('John', 'Doe', 'john.doe@email.com')
    """
)

# query database
cursor.execute("SELECT rowid, * FROM customers")
print(cursor.fetchone())

# create customers
customers = [
    ("Jane", "Doe", "jane.doe@email.com"),
    ("Bob", "Smith", "bob.smith@email.com"),
    ("Emma", "Williams", "emma.williams@email.com"),
    ("Olivia", "Brown", "olivia.brown@email.com"),
    ("Ava", "Jones", "ava.jones@email.com"),
    ("Isabella", "Miller", "isabella.miller@email.com"),
    ("Sophia", "Davis", "sophia.davis@email.com"),
    ("Mia", "Garcia", "mia.garcia@email.com"),
    ("Charlotte", "Rodriguez", "charlotte.rodriguez@email.com"),
    ("Amelia", "Wilson", "amelia.wilson@email.com"),
    ("Harper", "Anderson", "harper.anderson@email.com"),
    ("Evelyn", "Taylor", "evelyn.taylor@email.com"),
]

cursor.executemany("INSERT INTO customers VALUES(?,?,?)", customers)

# query database
cursor.execute("SELECT rowid, * FROM customers")
print("--Fetch one--")
print(cursor.fetchone())
print("--Fetch three--")
print(cursor.fetchmany(3))
print("--Fetch all--")
items = cursor.fetchall()
for item in items:
    print(item)

# save changes to database
conn.commit()

# close connection
conn.close()
