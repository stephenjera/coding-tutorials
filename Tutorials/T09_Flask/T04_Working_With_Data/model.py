"""Code to load json data"""
import json


def load_db():
    """Load json data

    Returns:
        dict: the data
    """
    with open("names.json","r", encoding="utf-8") as f:
        return json.load(f)


db = load_db()
