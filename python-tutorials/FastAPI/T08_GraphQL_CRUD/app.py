from fastapi import FastAPI
from sqlmodel import SQLModel, Field, create_engine, Session
from strawberry.fastapi import GraphQLRouter
from typing import List, Optional
import strawberry
import uvicorn

app = FastAPI()


@strawberry.type
class PersonType:
    id: int
    first_name: str
    last_name: str
    age: int


class Person(SQLModel, table=True):
    __table_args__ = {"extend_existing": True}
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    age: int


engine = create_engine(
    "sqlite:///database.sqlite",
    echo=True,
    connect_args={"check_same_thread": False},
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@strawberry.type
class Query:
    # Define a resolver function for the people field that returns a list of all people
    @strawberry.field
    def people(self) -> List[PersonType]:
        # Create a new session to interact with the database
        with Session(engine) as session:
            # Query the database for all people
            people = session.query(Person).all()
            return people

    # Define a resolver function for the person field that returns a single person by ID
    @strawberry.field
    def person(self, id: int) -> Optional[PersonType]:
        # Create a new session to interact with the database
        with Session(engine) as session:
            # Query the database for a person with the given ID
            person = session.get(Person, id)
            return person


@strawberry.type
class Mutation:
    # Define a resolver function for the addPerson field that creates a new person and returns it
    @strawberry.mutation
    def add_person(self, first_name: str, last_name: str, age: int) -> PersonType:
        # Create a new Person object using the provided arguments
        person = Person(first_name=first_name, last_name=last_name, age=age)

        # Create a new session to interact with the database
        with Session(engine) as session:
            # Add the new person to the database and commit the changes
            session.add(person)
            session.commit()
            # Refresh the person object to get its ID from the database
            session.refresh(person)

        return person

    # Define a resolver function for the updatePerson field that updates an existing person and returns it
    @strawberry.mutation
    def update_person(
        self,
        id: int,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        age: Optional[int] = None,
    ) -> Optional[PersonType]:
        # Create a new session to interact with the database
        with Session(engine) as session:
            # Query the database for a person with the given ID
            person = session.get(Person, id)

            if person is not None:
                # Update the person's fields using the provided arguments if they are not None
                if first_name is not None:
                    person.first_name = first_name
                if last_name is not None:
                    person.last_name = last_name
                if age is not None:
                    person.age = age

                # Add the updated person to the database and commit the changes
                session.add(person)
                session.commit()
                # Refresh the person object to get its updated state from the database
                session.refresh(person)

            return person

    # Define a resolver function for the deletePerson field that deletes an existing person and returns True if successful or False otherwise.
    @strawberry.mutation
    def delete_person(self, id: int) -> bool:
        # Create a new session to interact with the database.
        with Session(engine) as session:
            # Query the database for a person with the given ID.
            person = session.get(Person, id)

            if person is not None:
                # Delete the person from the database and commit the changes.
                session.delete(person)
                session.commit()
                return True
            else:
                return False


schema = strawberry.Schema(query=Query, mutation=Mutation)
app.include_router(GraphQLRouter(schema=schema, path="/"))

if __name__ == "__main__":
    uvicorn.run("app:app", reload=False, port=3000)
