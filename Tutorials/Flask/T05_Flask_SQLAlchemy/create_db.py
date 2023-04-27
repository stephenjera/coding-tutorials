from app import app, db, User
import sqlite3


with app.app_context():
    db.create_all()

# connect to database or create if not found
conn = sqlite3.connect("db.sqlite3")

# create a cursor
cursor = conn.cursor()

cursor.execute(
    """
    INSERT INTO user (username, email, date_joined)
    VALUES (?, ?, datetime('now'))
    """,
    ("john_doe", "john.doe@email.com"),
)


# save changes to database
conn.commit()

# close connection
conn.close()
