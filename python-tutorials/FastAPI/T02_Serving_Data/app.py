import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()
db = [
    {"id": 1, "size": "s", "fuel": "gasoline", "doors": 3, "transmission": "auto"},
    {"id": 2, "size": "s", "fuel": "electric", "doors": 3, "transmission": "auto"},
    {"id": 3, "size": "s", "fuel": "gasoline", "doors": 5, "transmission": "manual"},
    {"id": 4, "size": "m", "fuel": "electric", "doors": 3, "transmission": "auto"},
    {"id": 5, "size": "m", "fuel": "hybrid", "doors": 5, "transmission": "auto"},
    {"id": 6, "size": "m", "fuel": "gasoline", "doors": 5, "transmission": "manual"},
    {"id": 7, "size": "l", "fuel": "diesel", "doors": 5, "transmission": "manual"},
    {"id": 8, "size": "l", "fuel": "electric", "doors": 5, "transmission": "auto"},
    {"id": 9, "size": "l", "fuel": "hybrid", "doors": 5, "transmission": "auto"},
]


@app.get("/api/cars")
def get_cars(size: str | None = None, doors: int | None = None) -> list:
    """
    This function returns a list of cars from the database
    If size is provided, the function returns only cars of that size
    If doors is provided, the function returns only cars with at least that many doors
    Args:
        size (str | None, optional): Defaults to None.
        doors (int | None, optional): Defaults to None.

    Returns:
        list: list of cars
    """
    result = db
    if size:
        result = [car for car in result if car["size"] == size]
    if doors:
        result = [car for car in result if car["doors"] >= doors]
    return result


@app.get("/api/cars/{id}")
def car_by_id(id: int) -> dict:
    """This function returns a single car from the database by its id

    Args:
        id (int): car id
    Raises:
        HTTPException: If no car with the given id is found, 
        an HTTPException with status code 404 is raised

    Returns:
        dict: car by id
    """
    result = [car for car in db if car["id"] == id]
    if result:
        return result[0]
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)
