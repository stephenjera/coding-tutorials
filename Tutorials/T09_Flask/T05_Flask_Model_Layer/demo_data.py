# run this at the beginning of the course

from pathlib import Path
from flask import current_app
from flaskr_carved_rock import create_app
from flaskr_carved_rock.db import get_db, init_db

app = create_app()
app.app_context().push()
init_db()
db = get_db()

with Path("demo_data.sql").open() as f:
        db.executescript(f.read())