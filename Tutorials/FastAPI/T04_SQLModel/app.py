import uvicorn
from typing import Optional
from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Hero(SQLModel, table=True):
    __table_args__ = {"extend_existing": True}
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str  # = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None)


engine = create_engine(
    f"sqlite:///database.sqlite",
    echo=True,
    connect_args={"check_same_thread": False},
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
def welcome():
    return {"hello": "hero"}


@app.get("/api/heroes/{hero_id}")
def read_hero(hero_id: int, session: Session = Depends(get_session)) -> Hero:
    # with Session(engine) as session:
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero


@app.get("/api/heroes/")
def read_heroes(session: Session = Depends(get_session)) -> list[Hero]:
    # with Session(engine) as session:
    heroes = session.exec(select(Hero)).all()
    return heroes


@app.post("/api/heroes/", response_model=Hero)
def add_hero(hero: Hero, session: Session = Depends(get_session)) -> Hero:
    # with Session(engine) as session:
    new_hero = Hero.from_orm(hero)
    session.add(new_hero)
    session.commit()
    session.refresh(new_hero)
    return new_hero


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)
