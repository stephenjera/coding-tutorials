"""Code to load json data"""
import json


def load_db():
    """Load json data

    Returns:
        dict: the data
    """
    with open("names.json", "r", encoding="utf-8") as f:
        return json.load(f)


def save_db():
    """Save json file

    Returns:
        dict: updated json file
    """
    with open("names.json", "w", encoding="utf-8") as f:
        return json.dump(db, f)


db = load_db()
