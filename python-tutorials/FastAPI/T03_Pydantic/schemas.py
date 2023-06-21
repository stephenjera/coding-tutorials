import json
from pydantic import BaseModel


class Car(BaseModel):
    # This class defines a Car model using Pydantic's BaseModel
    # The Car model has five fields: id, size, fuel, doors, and transmission
    id: int
    size: str
    fuel: str | None = "electric"
    doors: int
    transmission: str | None = "auto"


def load_db() -> list[Car]:
    """Load a list of Car objects from a JSON file"""
    with open("cars.json") as f:
        return [Car.parse_obj(obj) for obj in json.load(f)]


def save_db(cars: list[Car]):
    with open("cars.json", "w") as f:
        json.dump([car.dict() for car in cars], f, indent=4)
